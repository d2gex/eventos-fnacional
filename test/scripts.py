import pandas as pd
from src import config
from src.db import utils as utils_db
from src.db import models, scripts as db_scripts


TEST_PATH = config.ROOT_PATH / "test"
TEST_DB_PATH = TEST_PATH / "stubs" / "nombre_apellidos_toreros.csv"


def add_toreros_testing_data(db_df: pd.DataFrame, max_rows: int):
    db_data = []
    for record in db_df.head(max_rows).to_dict(orient="records"):
        record[
            "nombre_profesional"
        ] = f"{record['nombre']} {record['apellidos']} {record ['apodo']}"
        record["tipo_torero_id"] = 1
        db_data.append(models.ModelTorero(**record))
    with utils_db.session_scope() as dbs:
        dbs.query(models.ModelTorero).delete()
        dbs.add_all(db_data)


def add_ganaderias(max_rows: int):
    db_data = [
        models.ModelGanaderia(nombre_ganaderia=f"Ganaderia_{x}", provincia_id=44)
        for x in range(max_rows)
    ]
    with utils_db.session_scope() as dbs:
        dbs.query(models.ModelGanaderia).delete()
        dbs.add_all(db_data)


if __name__ == "__main__":
    db_scripts.create_init_db()
    toreros_df = pd.read_csv(TEST_DB_PATH)
    add_toreros_testing_data(toreros_df, 500)
    add_ganaderias(100)
