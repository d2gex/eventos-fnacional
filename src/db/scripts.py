import pandas as pd
from pathlib import Path
from typing import Optional, List
from src.db import utils as utils_db
from src.db import models
from src import config


class SqlLitDBSetup:
    def init_database(self) -> None:
        models.ModelBase.metadata.drop_all(utils_db.engine)
        models.ModelBase.metadata.create_all(utils_db.engine)

    def init_tipo_torero_table(self) -> None:
        db_data = [
            models.ModelTipoTorero(tipo_torero=x) for x in ["Torero", "Rejoneador"]
        ]
        with utils_db.session_scope() as dbs:
            dbs.add_all(db_data)

    def init_provincia_table(self, csv_path: str) -> None:
        provincia_df = pd.read_csv(csv_path)
        db_data = [models.ModelProvincia(provincia=x) for x in provincia_df.name.values]
        with utils_db.session_scope() as dbs:
            dbs.add_all(db_data)

    def run(self):
        self = SqlLitDBSetup()
        print("Start setting the sql database ....")
        if config.Config.CREATE_SQL_DATABASE:
            print("-----------> Creating the database")
            self.init_database()
        print("-----------> Adding initial tipo toreros")
        self.init_tipo_torero_table()
        print("-----------> Adding provincias")
        self.init_provincia_table(config.DATA_PATH / "provincias_es.csv")
        print("... Sql database set up")


class CsvDBSetup:
    def __init__(self, db_path_original: Path, db_path_new: Path):
        self.db_path_original = db_path_original
        self.db_path_new = db_path_new

    def _extract_data_from_excel(
        self,
        sheet_name: str,
        col_range: List[str],
        skip_rows: int,
        num_rows: int,
        header=Optional[List[str]],
    ):
        col_range = ":".join(col_range)
        data = pd.read_excel(
            self.db_path_original,
            sheet_name=sheet_name,
            usecols=col_range,
            skiprows=skip_rows,
            nrows=num_rows,
            names=header,
        )
        return data

    def amalgamate_all_sheets(self):
        db = pd.ExcelFile(self.db_path_original)
        sheet_names = db.sheet_names[1:]
        df = pd.concat([db.parse(sheet) for sheet in sheet_names[1:]])
        return df

    def run(self):
        print("Start setting the csv database ....")
        db_df = old_db_setup.amalgamate_all_sheets()
        db_df.to_csv(self.db_path_new)
        print("... Csv database set up")


if __name__ == "__main__":
    if config.Config.CREATE_CSV_DATABASE:
        old_db_setup = CsvDBSetup(
            config.Config.ORIGINAL_CSV_DB_PATH, config.Config.NEW_CSV_DB_PATH
        )
        old_db_setup.run()

    if config.Config.CREATE_SQL_DATABASE:
        sql_db_setup = SqlLitDBSetup()
        sql_db_setup.run()
