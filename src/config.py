import os
from pathlib import Path
from dotenv import load_dotenv

file_path = Path(__file__).resolve()
ROOT_PATH = file_path.parents[1]
DATA_PATH = ROOT_PATH / "data"
SRC_PATH = ROOT_PATH / "src"
DB_PATH = DATA_PATH / "sensitive"
load_dotenv(SRC_PATH / ".env")


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DB_NAME = os.getenv("DB_NAME")
    CREATE_SQL_DATABASE = os.getenv("CREATE_SQL_DATABASE")
    CREATE_CSV_DATABASE = os.getenv("CREATE_CSV_DATABASE")
    ORIGINAL_CSV_DB_PATH = DATA_PATH / "sensitive" / os.getenv("CSV_OLD_DB_NAME")
    NEW_CSV_DB_PATH = DATA_PATH / "sensitive" / os.getenv("CSV_NEW_DB_NAME")
