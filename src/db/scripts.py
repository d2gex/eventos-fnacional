import pandas as pd
import re
from typing import List
from pathlib import Path
from src.db import utils as utils_db
from src.db import models
from src import config


class SqlLitDBSetup:
    def __init__(
        self,
        tipo_toreros: List[str],
        tipo_premios: List[str],
        tipo_estados: List[str],
        provincias_path: Path,
        poblaciones_path: Path,
        old_db: pd.DataFrame,
    ):
        self.tipo_toreros = tipo_toreros
        self.tipo_premios = tipo_premios
        self.tipo_estados = tipo_estados
        self.provincias_path = provincias_path
        self.poblaciones_path = poblaciones_path
        self.old_db = old_db

    def init_database(self) -> None:
        models.ModelBase.metadata.drop_all(utils_db.engine)
        models.ModelBase.metadata.create_all(utils_db.engine)

    def init_tipo_torero_table(self) -> None:
        db_data = [models.ModelTipoTorero(tipo_torero=x) for x in self.tipo_toreros]
        with utils_db.session_scope() as dbs:
            dbs.add_all(db_data)

    def init_tipo_premios_table(self) -> None:
        db_data = [models.ModelTipoPremio(tipo_premio=x) for x in self.tipo_premios]
        with utils_db.session_scope() as dbs:
            dbs.add_all(db_data)

    def init_tipo_estado_table(self) -> None:
        db_data = [models.ModelTipoEstado(tipo_estado=x) for x in self.tipo_estados]
        with utils_db.session_scope() as dbs:
            dbs.add_all(db_data)

    def init_provincia_table(self) -> None:
        provincia_df = pd.read_csv(self.provincias_path)
        db_data = [models.ModelProvincia(provincia=x) for x in provincia_df.name.values]
        with utils_db.session_scope() as dbs:
            dbs.add_all(db_data)

    def init_problacion_table(self, provincia_id=45) -> None:
        poblacion_df = pd.read_csv(self.poblaciones_path)
        db_data = [
            models.ModelPoblacion(ciudad=x, provincia_id=provincia_id)
            for x in poblacion_df.name.values
        ]
        with utils_db.session_scope() as dbs:
            dbs.add_all(db_data)

    def init_tipo_festejos(self):
        # Only word characters and white spaces are allowed
        tipo_festejos = set(
            re.sub(r"([^\w\s-]+)", "", y)
            for y in [x.lower().title().strip() for x in self.old_db["Tipo"].dropna()]
        )
        # Get rid of whitespaces
        tipo_festejos = list(filter(None, tipo_festejos))

        # Store it into the database
        db_data = [models.ModelTipoFestejo(tipo_festejo=x) for x in tipo_festejos]
        with utils_db.session_scope() as dbs:
            dbs.add_all(db_data)

    def run(self):
        print("Start setting the sql database ....")
        if config.Config.CREATE_SQL_DATABASE:
            print("-----------> Creating the database")
            self.init_database()
        print("-----------> Adding initial tipo toreros")
        self.init_tipo_torero_table()
        print("-----------> Adding initial tipo premios")
        self.init_tipo_premios_table()
        print("-----------> Adding initial tipo estados")
        self.init_tipo_estado_table()
        print("-----------> Adding provincias")
        self.init_provincia_table()
        print("-----------> Adding poblaciones")
        self.init_problacion_table()
        print("-----------> Adding initial tipo festejos")
        self.init_tipo_festejos()
        print("... Sql database set up")


class CsvDBSetup:
    def __init__(
        self,
        db_path_original: Path,
        db_path_new: Path,
    ):
        self.db_path_original = db_path_original
        self.db_path_new = db_path_new

    def amalgamate_all_sheets(self):
        db = pd.ExcelFile(self.db_path_original)
        sheet_names = db.sheet_names[1:]
        df = pd.concat([db.parse(sheet) for sheet in sheet_names[1:]])
        return df

    def run(self) -> pd.DataFrame:
        print("Start setting the csv database ....")
        db_df = self.amalgamate_all_sheets()
        db_df = db_df.rename(
            columns={"Dis s.": "Dia Semana", "Ver fecha real": "Fecha Real"}
        )
        db_df = db_df.dropna(how="all")
        db_df["id"] = list(range(1, len(db_df) + 1))
        db_df.to_csv(self.db_path_new, index=False)
        print("... Csv database set up")
        return db_df


def create_init_db():
    if config.Config.CREATE_CSV_DATABASE:
        old_db_setup = CsvDBSetup(
            config.Config.ORIGINAL_CSV_DB_PATH, config.Config.NEW_CSV_DB_PATH
        )
        old_db_df = old_db_setup.run()

    if config.Config.CREATE_SQL_DATABASE:
        sql_db_setup = SqlLitDBSetup(
            tipo_toreros=["Torero", "Rejoneador"],
            tipo_premios=["N", "O", "OO", "OOR"],
            tipo_estados=["Nada", "Herido", "1 aviso", "2 avisos", "3 avisos"],
            provincias_path=config.DATA_PATH / "provincias_es.csv",
            poblaciones_path=config.DATA_PATH / "poblaciones_toledo.csv",
            old_db=old_db_df,
        )
        sql_db_setup.run()


if __name__ == "__main__":
    create_init_db()
