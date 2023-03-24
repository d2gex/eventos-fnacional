from pathlib import Path
from os import path

file_path = Path(__file__).resolve()
ROOT_PATH = str(file_path.parents[1])
DATA_PATH = path.join(ROOT_PATH, 'data')
SRC_PATH = path.join(ROOT_PATH, 'src')
DB_PATH = path.join(SRC_PATH, 'db')
DB_NAME = 'eventos_taurinos.db'

original_db_path = path.join(DATA_PATH, 'original_database.xls')
