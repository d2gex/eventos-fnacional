import pandas as pd
from src.db import utils as utils_db
from src.db import models
from src import config


def init_database() -> None:
    models.ModelBase.metadata.drop_all(utils_db.engine)
    models.ModelBase.metadata.create_all(utils_db.engine)


def init_tipo_torero_table() -> None:
    db_data = [models.ModelTipoTorero(tipo_torero=x) for x in ["Torero", "Rejoneador"]]
    with utils_db.session_scope() as dbs:
        dbs.add_all(db_data)


def init_provincia_table(csv_path: str) -> None:
    provincia_df = pd.read_csv(csv_path)
    db_data = [models.ModelProvincia(provincia=x) for x in provincia_df.name.values]
    with utils_db.session_scope() as dbs:
        dbs.add_all(db_data)


if __name__ == "__main__":
    print("Start setting the database ....")
    if config.Config.CREATE_DATABASE:
        print("-----------> Creating the database")
        init_database()
    print("-----------> Adding initial tipo toreros")
    init_tipo_torero_table()
    print("-----------> Adding provincias")
    init_provincia_table(config.DATA_PATH / "provincias_es.csv")
    print("... Database set up")
