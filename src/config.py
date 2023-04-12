import os
from pathlib import Path
from dotenv import load_dotenv

file_path = Path(__file__).resolve()
ROOT_PATH = file_path.parents[1]
DATA_PATH = ROOT_PATH / 'data'
SRC_PATH = ROOT_PATH / 'src'
DB_PATH = DATA_PATH / 'sensitive'

original_db_path = DATA_PATH / 'sensitive' / 'original_database.xls'
load_dotenv(SRC_PATH / '.env')


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DB_NAME = os.getenv('DB_NAME')
    CREATE_DATABASE = os.getenv('CREATE_DATABASE')
