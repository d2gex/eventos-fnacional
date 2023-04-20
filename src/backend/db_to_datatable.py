from typing import List, Dict
from collections import defaultdict


class DbToDataTable:
    def get_rows_by_festejo(self, data: List[Dict]) -> Dict[int, List]:
        festejos = defaultdict(list)
        for item in data:
            festejos[item[0]].append(item)
        return festejos

    def segregate_festejo_by_variables(self, data: Dict[int, List]) -> Dict:
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

                if (
                    row[to_offset] not in toreros
                ):  # first time we encounter this torero?
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

    def discern_premios_by_torero_and_festejo(self, data: Dict) -> Dict:
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

    def build_festejos_table(self, data: Dict) -> List[Dict]:
        table = []
        for festejo_id, festejo_rows in data.items():
            table.append(
                {
                    "id": festejo_id,
                    "nombre": festejo_rows["nombre_festejo"].title(),
                    "poblacion": festejo_rows["poblacion"].title(),
                    "fecha": festejo_rows["fecha_festejo"].strftime("%d-%m-%Y"),
                    "toreros": ", ".join([x.title() for x in festejo_rows["toreros"]]),
                    "ganaderias": ", ".join(
                        [x.title() for x in festejo_rows["ganaderias"]]
                    ),
                    "premios": ", ".join(
                        str(item) for _, item in festejo_rows["toreros_premios"].items()
                    ),
                    "notas": festejo_rows["notas"],
                }
            )
        return table

    def run(self, data: List[Dict]) -> List[Dict]:
        result = self.get_rows_by_festejo(data)
        result = self.segregate_festejo_by_variables(result)
        result = self.discern_premios_by_torero_and_festejo(result)
        table = self.build_festejos_table(result)
        return table
