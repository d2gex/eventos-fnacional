from typing import List, Dict, Tuple, Any, Optional
from src.db import models
from src.db import utils as utils_db
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError
from datetime import datetime


class ApiDB:
    @classmethod
    def get_table(cls, model: Any) -> List[Dict]:
        with utils_db.session_scope() as dbs:
            db_data = dbs.query(model).all()
            data = [x.to_dict() for x in db_data]
        return data

    @classmethod
    def get_toreros(cls) -> Tuple[List[Tuple], List[str]]:
        m = models
        columns = [
            m.ModelTorero.id,
            m.ModelTorero.nombre_profesional,
            m.ModelTorero.nombre,
            m.ModelTorero.apellidos,
            m.ModelTorero.apodo,
            m.ModelTorero.tipo_torero_id,
            m.ModelTipoTorero.tipo_torero,
        ]
        column_names = [c.key for c in columns]
        with utils_db.session_scope() as db_session:
            db_data = (
                db_session.query(*columns)
                .join(
                    m.ModelTorero,
                    m.ModelTipoTorero.id == m.ModelTorero.tipo_torero_id,
                )
                .order_by(m.ModelTorero.id.desc())
                .all()
            )
        return db_data, column_names

    @classmethod
    def get_all_festejos(cls, premios_or_estados: bool):
        m = models
        columns = [
            m.ModelFestejo.id,
            m.ModelFestejo.nombre_festejo,
            m.ModelFestejo.fecha,
            m.ModelFestejo.notas,
            m.ModelGanaderia.nombre_ganaderia,
            m.ModelPoblacion.ciudad,
            m.ModelTorero.nombre_profesional,
            m.ModelTipoTorero.tipo_torero,
        ]
        columns.extend(
            [
                m.ModelTipoPremio.id,
                m.ModelTipoPremio.tipo_premio,
            ]
            if premios_or_estados
            else [
                m.ModelTipoEstado.id,
                m.ModelTipoEstado.tipo_estado,
            ]
        )

        with utils_db.session_scope() as db_session:
            query = (
                db_session.query(*columns)
                .join(  # Get Ganaderias associated to festejos
                    m.ModelGanaderiaFestejo,
                    m.ModelFestejo.id == m.ModelGanaderiaFestejo.festejo_id,
                )
                .join(
                    m.ModelGanaderia,
                    m.ModelGanaderiaFestejo.ganaderia_id == m.ModelGanaderia.id,
                )
                .join(
                    m.ModelPoblacion, m.ModelFestejo.poblacion_id == m.ModelPoblacion.id
                )
                .join(  # Festejos with Toreros
                    m.ModelToreroFestejo,
                    m.ModelFestejo.id == m.ModelToreroFestejo.festejo_id,
                )
                .join(m.ModelTorero, m.ModelToreroFestejo.torero_id == m.ModelTorero.id)
                .join(
                    m.ModelTipoTorero,
                    m.ModelTorero.tipo_torero_id == m.ModelTipoTorero.id,
                )
            )

            if premios_or_estados:  # Festejos y Toreros with premios
                query = query.join(
                    m.ModelToreroPremioFestejo,
                    and_(
                        m.ModelToreroFestejo.festejo_id
                        == m.ModelToreroPremioFestejo.festejo_id,
                        m.ModelToreroFestejo.torero_id
                        == m.ModelToreroPremioFestejo.torero_id,
                    ),
                ).join(
                    m.ModelTipoPremio,
                    m.ModelToreroPremioFestejo.tipo_premio_id == m.ModelTipoPremio.id,
                )
            else:  # Festejos y Toreros with Estados
                query = query.join(
                    m.ModelToreroEstadoFestejo,
                    and_(
                        m.ModelToreroFestejo.festejo_id
                        == m.ModelToreroEstadoFestejo.festejo_id,
                        m.ModelToreroFestejo.torero_id
                        == m.ModelToreroEstadoFestejo.torero_id,
                    ),
                ).join(
                    m.ModelTipoEstado,
                    m.ModelToreroEstadoFestejo.tipo_estado_id == m.ModelTipoEstado.id,
                )

        db_data = query.order_by(m.ModelTorero.id).order_by(m.ModelGanaderia.id).all()
        return db_data

    @classmethod
    def getGanaderias(cls) -> Tuple[List[Tuple], List[str]]:
        m = models
        columns = [
            m.ModelGanaderia.id,
            m.ModelGanaderia.nombre_ganaderia,
            m.ModelGanaderia.provincia_id,
            m.ModelProvincia.provincia,
        ]
        column_names = [c.key for c in columns]
        with utils_db.session_scope() as db_session:
            db_data = (
                db_session.query(*columns)
                .join(
                    m.ModelProvincia,
                    m.ModelGanaderia.provincia_id == m.ModelProvincia.id,
                )
                .order_by(m.ModelGanaderia.id.desc())
                .all()
            )
        return db_data, column_names

    @classmethod
    def save_torero_details(cls, data: Dict) -> Optional[Dict]:
        try:
            for torero_details in data["toreroRow"]:
                with utils_db.session_scope() as s_db:
                    torero_details[
                        "nombre_profesional"
                    ] = f"{torero_details['nombre']} {torero_details['apellidos']} {torero_details['apodo']}".strip()
                    if torero_details["id"] is None:  # insert
                        del torero_details["id"]
                        s_db.add(models.ModelTorero(**torero_details))
                    else:  # update
                        s_db.merge(models.ModelTorero(**torero_details))
        except IntegrityError:
            result = torero_details
        else:
            result = None
        return result

    @classmethod
    def save_ganaderia_details(cls, data: Dict) -> Optional[Dict]:
        try:
            for ganaderia_details in data["ganaderiaRow"]:
                with utils_db.session_scope() as s_db:
                    if ganaderia_details["id"] is None:  # insert
                        del ganaderia_details["id"]
                        s_db.add(models.ModelGanaderia(**ganaderia_details))
                    else:  # update
                        s_db.merge(models.ModelGanaderia(**ganaderia_details))
        except IntegrityError:
            result = ganaderia_details
        else:
            result = None
        return result

    @classmethod
    def save_festejo(cls, data: Dict, db_session: Any) -> int:
        data["fecha"] = datetime.strptime(data["fecha"], "%d/%m/%Y").date()
        festejo = models.ModelFestejo(**data)
        db_session.add(festejo)
        db_session.flush()
        return festejo.id

    @classmethod
    def save_ganaderia_festejos(
        cls, data: List[Dict], festejo_id: int, db_session: Any
    ):
        db_data = [
            models.ModelGanaderiaFestejo(
                ganaderia_id=ganaderia_details["ganaderiaName"]["id"],
                festejo_id=festejo_id,
            )
            for ganaderia_details in data
        ]
        db_session.add_all(db_data)

    @classmethod
    def save_torero_festejos(cls, data: List[Dict], festejo_id: int, db_session: Any):
        db_data = [
            models.ModelToreroFestejo(
                torero_id=torero_details["toreroName"]["id"],
                festejo_id=festejo_id,
            )
            for torero_details in data
        ]
        db_session.add_all(db_data)

    @classmethod
    def save_torero_premios_by_festejos(
        cls, data: List[Dict], festejo_id: int, db_session: Any
    ):
        toreros_premios_data = []
        for row in data:
            torero_details = row["toreroName"]
            torero_premios = row["premios"]
            for index, premio_instance in enumerate(torero_premios):
                toreros_premios_data.append(
                    {
                        "festejo_id": festejo_id,
                        "torero_id": torero_details["id"],
                        "tipo_premio_id": premio_instance,
                        "faena": index,
                    }
                )
        db_data = [
            models.ModelToreroPremioFestejo(**premio_row)
            for premio_row in toreros_premios_data
        ]
        db_session.add_all(db_data)

    @classmethod
    def save_torero_estados_by_festejos(
        cls, data: List[Dict], festejo_id: int, db_session: Any
    ):
        toreros_estados_data = []
        for row in data:  # Array of toreros
            torero_details = row["toreroName"]
            torero_estados = row["estados"]
            for index, multiple_estados in enumerate(
                torero_estados
            ):  # Array of multiple estados (Heridos, 1 aviso, etc..)
                for estado in multiple_estados:  # Each individual estado
                    toreros_estados_data.append(
                        {
                            "festejo_id": festejo_id,
                            "torero_id": torero_details["id"],
                            "tipo_estado_id": estado["id"],
                            "faena": index,
                        }
                    )
        db_data = [
            models.ModelToreroEstadoFestejo(**estados_row)
            for estados_row in toreros_estados_data
        ]
        db_session.add_all(db_data)

    @classmethod
    def save_festejos(cls, data: Dict) -> Optional[str]:
        data["festejos"].pop("provincia_id")
        try:
            with utils_db.session_scope() as s_db:
                festejo_id = cls.save_festejo(data["festejos"], s_db)
                cls.save_ganaderia_festejos(data["ganaderiaRow"], festejo_id, s_db)
                cls.save_torero_festejos(data["toreroRow"], festejo_id, s_db)
                cls.save_torero_premios_by_festejos(data["toreroRow"], festejo_id, s_db)
                cls.save_torero_estados_by_festejos(data["toreroRow"], festejo_id, s_db)
        except IntegrityError as ex:
            if "torero_festejo" in str(ex):
                error = "toreros"
            else:
                error = "ganaderias"
        else:
            error = None
        return error
