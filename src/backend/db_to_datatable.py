from typing import List, Dict, Tuple
from collections import defaultdict


class FestejosToDataTable:
    def get_rows_by_festejo(self, data: List[Dict]) -> Dict[int, List]:
        festejos = defaultdict(list)
        for item in data:
            festejos[item[0]].append(item)
        return festejos

    def segregate_festejo_by_variables(self, data: Dict[int, List]) -> Dict:
        festejos = {}
        g_offset, to_offset, pr_or_es_offset, faena_offset = 4, 6, 9, 10
        nom_offset, fe_offset, no_offset, po_offset = 1, 2, 3, 5
        for festejo_id, festejo_rows in data.items():
            ganaderias = set()
            toreros = set()
            torero_pr_or_es = {}
            nombre = ""
            fecha = ""
            notas = ""
            poblacion = ""
            festejos[festejo_id] = {}
            ganaderia = None
            for row in festejo_rows:
                ganaderias.add(row[g_offset])

                if (
                    row[to_offset] not in toreros
                ):  # first time we encounter this torero?
                    torero_pr_or_es[row[to_offset]] = []
                    ganaderia = row[g_offset]

                # We are only interested in the premio or estado combination per torero and per one single ganaderia
                if ganaderia == row[g_offset]:
                    torero_pr_or_es[row[to_offset]].append(
                        (row[g_offset], row[pr_or_es_offset], row[faena_offset])
                    )

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
                "toreros_pr_or_es": torero_pr_or_es,  # {'torero_id': [(G,P,F), ...]}; G=Ganaderia, P=Premio, F=Faena
            }
        return festejos

    def group_pr_or_es_by_faena(self, festejos: Dict):
        """Create a list of grouped premios or estados per torero and faena. The length of grouped premios will always be a
        list of length 1. Estados could have groups of multiple items
        """
        g_offset, pr_or_es_offset, faena_offset = 0, 1, 2
        for festejo_id, festejo_row in festejos.items():
            # Get list of tuples [(G, P, F)...] as a dictionary of lists by F { F: [(G, P)...]
            for torero_id, torero_row in festejo_row["toreros_pr_or_es"].items():
                faenas = {}
                for list_item in torero_row:
                    faena_id = list_item[faena_offset]
                    if (
                        faena_id not in faenas.keys()
                    ):  # first time of record? create a list
                        faenas[faena_id] = []
                    faenas[faena_id].append(
                        (list_item[g_offset], list_item[pr_or_es_offset])
                    )
                # Flatten the dictionary of lists into a list of lists of tuples [[(G, P), ...], [(G, P), ...]]
                festejo_row["toreros_pr_or_es"][torero_id] = [
                    g_pr_or_es_list for _, g_pr_or_es_list in faenas.items()
                ]
        return festejos

    def build_list_of_pr_or_es_indicators_by_torero(self, data: Dict) -> Dict:
        g_offset, pr_or_es_offset = 0, 1
        for festejo_id, festejo_rows in data.items():
            for torero_id, pr_or_es_lists in festejo_rows["toreros_pr_or_es"].items():
                premios_or_estados = []
                for list_item in pr_or_es_lists:
                    grouped_items = []
                    for tuple_item in list_item:
                        grouped_items.append(tuple_item[pr_or_es_offset])

                    premios_or_estados.append(
                        tuple(grouped_items)
                        if len(grouped_items) > 1
                        else grouped_items.pop()
                    )
                festejo_rows["toreros_pr_or_es"][torero_id] = premios_or_estados
        return data

    def build_festejo_by_pr_or_es(self, data: Dict, pr_or_es_key: bool) -> List[Dict]:
        festejo = []
        if pr_or_es_key:
            field = "premios"
        else:
            field = "estados"
        for festejo_id, festejo_rows in data.items():
            festejo.append(
                {
                    "id": festejo_id,
                    "nombre": festejo_rows["nombre_festejo"].title(),
                    "poblacion": festejo_rows["poblacion"].title(),
                    "fecha": festejo_rows["fecha_festejo"].strftime("%d-%m-%Y"),
                    "toreros": ", ".join([x.title() for x in festejo_rows["toreros"]]),
                    "notas": festejo_rows["notas"],
                    "ganaderias": ", ".join(
                        [x.title() for x in festejo_rows["ganaderias"]]
                    ),
                    field: ", ".join(
                        str(item)
                        for _, item in festejo_rows["toreros_pr_or_es"].items()
                    ),
                }
            )
        return festejo

    def build_table_festejo(self, data: List[Dict], pr_or_es_key: bool) -> List[Dict]:
        result = self.get_rows_by_festejo(data)
        result = self.segregate_festejo_by_variables(result)
        result = self.group_pr_or_es_by_faena(result)
        result = self.build_list_of_pr_or_es_indicators_by_torero(result)
        table = self.build_festejo_by_pr_or_es(result, pr_or_es_key)
        return table

    def run(self, data_with_premios: List[Dict], data_with_estados: List[Dict]):
        festejos = self.build_table_festejo(data_with_premios, pr_or_es_key=True)
        festejos_estados = self.build_table_festejo(
            data_with_estados, pr_or_es_key=False
        )
        for index in range(len(festejos)):
            festejos[index]["estados"] = festejos_estados[index]["estados"]
        return festejos


class DbToDataTable:
    def __init__(self, keys: List[str], data: List[Tuple]):
        self.keys = keys
        self.data = data

    def __call__(self, *args, **kwargs):
        return [dict([(k, v) for k, v in zip(self.keys, row)]) for row in self.data]


class GanaderiasToDataTable(DbToDataTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TorerosToDataTable(DbToDataTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
