import pandas as pd
from src.db import models as m, utils as utils_db
from sqlalchemy import and_
from typing import List, Dict
from collections import defaultdict


def get_db_data():
    with utils_db.session_scope() as db_session:
        db_data = (
            db_session.query(
                m.ModelFestejo.id,
                m.ModelFestejo.nombre_festejo,
                m.ModelFestejo.fecha,
                m.ModelFestejo.notas,
                m.ModelGanaderia.nombre_ganaderia,
                m.ModelPoblacion.ciudad,
                m.ModelTorero.nombre_profesional,
                m.ModelTipoTorero.tipo_torero,
                m.ModelTipoPremio.tipo_premio,
            )
            # Get Ganaderias associated to festejos
            .join(
                m.ModelGanaderiaFestejo,
                m.ModelFestejo.id == m.ModelGanaderiaFestejo.festejo_id,
            )
            .join(
                m.ModelGanaderia,
                m.ModelGanaderiaFestejo.ganaderia_id == m.ModelGanaderia.id,
            )
            .join(m.ModelPoblacion, m.ModelFestejo.poblacion_id == m.ModelPoblacion.id)
            # Festejos with Toreros
            .join(
                m.ModelToreroFestejo,
                m.ModelFestejo.id == m.ModelToreroFestejo.festejo_id,
            )
            .join(m.ModelTorero, m.ModelToreroFestejo.torero_id == m.ModelTorero.id)
            .join(
                m.ModelTipoTorero, m.ModelTorero.tipo_torero_id == m.ModelTipoTorero.id
            )
            # Festejos y Toreros with Premios
            .join(
                m.ModelToreroPremioFestejo,
                and_(
                    m.ModelToreroFestejo.festejo_id
                    == m.ModelToreroPremioFestejo.festejo_id,
                    m.ModelToreroFestejo.torero_id
                    == m.ModelToreroPremioFestejo.torero_id,
                ),
            )
            .join(
                m.ModelTipoPremio,
                m.ModelToreroPremioFestejo.tipo_premio_id == m.ModelTipoPremio.id,
            )
            .all()
        )
    return db_data


def get_rows_by_festejo(data: List[Dict]) -> Dict[int, List]:
    festejos = defaultdict(list)
    for item in data:
        festejos[item[0]].append(item)
    return festejos


def segregate_festejo_by_variables(data: Dict[int, List]) -> Dict:
    festejos = {}
    g_offset, to_offset, pr_offset = 4, 6, 8
    nom_offset, fe_offset, no_offset, po_offset = 1, 2, 3, 5
    for festejo_id, festejo_rows in data.items():
        ganaderias = set()
        toreros = set()
        torero_premios = {}
        nombre = ""
        fecha = ""
        notas = ""
        poblacion = ""
        festejos[festejo_id] = {}
        for row in festejo_rows:
            ganaderias.add(row[g_offset])

            if row[to_offset] not in toreros:  # first time we encounter this torero?
                torero_premios[row[to_offset]] = []

            torero_premios[row[to_offset]].append((row[g_offset], row[pr_offset]))
            toreros.add(row[to_offset])
            nombre = row[nom_offset]
            fecha = row[fe_offset]
            notas = row[no_offset]
            poblacion = row[po_offset]

        festejos[festejo_id] = {
            "nombre_festejo": nombre,
            "fecha_festejo": fecha,
            "poblacion": poblacion,
            "notas": notas,
            "ganaderias": ganaderias,  # unique ganaderias per festejo
            "toreros": toreros,  # unique toreros per festejo
            "toreros_premios": torero_premios,  # {'torero_id': [(G,P), ...]}; G=Ganaderia, P=Premio
        }
    return festejos


def discern_premios_by_torero_and_festejo(data: Dict) -> Dict:
    g_offset, pr_offset = 0, 1
    for festejo_id, festejo_rows in data.items():
        for torero_id, premio_ganaderia in festejo_rows["toreros_premios"].items():
            ganaderia = premio_ganaderia[0][g_offset]
            premios = []
            for row in premio_ganaderia:
                if (
                    row[g_offset] == ganaderia
                ):  # Get only the premios for one ganaderia, rest is duplicated
                    premios.append(row[pr_offset])
            festejo_rows["toreros_premios"][torero_id] = premios
    return data


def build_festejos_table(data: Dict) -> List[Dict]:
    table = []
    for festejo_id, festejo_rows in data.items():
        table.append(
            {
                "id": festejo_id,
                "nombre": festejo_rows["nombre_festejo"],
                "poblacion": festejo_rows["poblacion"],
                "fecha": festejo_rows["fecha_festejo"],
                "toreros": ", ".join(festejo_rows["toreros"]),
                "ganaderias": ", ".join(festejo_rows["ganaderias"]),
                "premios": ", ".join(
                    str(item) for _, item in festejo_rows["toreros_premios"].items()
                ),
                "notas": festejo_rows["notas"],
            }
        )
    return table


if __name__ == "__main__":
    data = get_db_data()
    result = get_rows_by_festejo(data)
    result = segregate_festejo_by_variables(result)
    unfolded_results = discern_premios_by_torero_and_festejo(result)
    print(build_festejos_table(unfolded_results))
    # print(unfolded_results)
