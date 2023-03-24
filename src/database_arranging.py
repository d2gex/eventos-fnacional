import pandas as pd
from typing import List, Optional
from src import config as cfg


def extract_data_from_excel(data_path: str, sheet_name: str, col_range: List[str], skip_rows: int, num_rows: int,
                            header=Optional[List]) -> pd.DataFrame:
    col_range = ':'.join(col_range)
    data = pd.read_excel(data_path, sheet_name=sheet_name, usecols=col_range, skiprows=skip_rows, nrows=num_rows,
                         names=header)
    return data


if __name__ == "__main__":
    xls = pd.ExcelFile(cfg.original_db_path)
    sheet_names = xls.sheet_names[1:]
    df_list = []
    for sheet_name in sheet_names:
        df_list.append(pd.read_excel(cfg.original_db_path, sheet_name=sheet_name))


