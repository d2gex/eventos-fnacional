import os
from pathlib import Path
from os import path
from dotenv import load_dotenv
from os.path import join

file_path = Path(__file__).resolve()
ROOT_PATH = str(file_path.parents[1])
DATA_PATH = path.join(ROOT_PATH, 'data')
SRC_PATH = path.join(ROOT_PATH, 'src')
DB_PATH = path.join(DATA_PATH, 'sensitive')

original_db_path = path.join(DATA_PATH, 'sensitive', 'original_database.xls')
load_dotenv(join(SRC_PATH, '.env'))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DB_NAME = os.getenv('DB_NAME')
    CREATE_DATABASE = os.getenv('CREATE_DATABASE')
