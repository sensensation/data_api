import pandas as pd
from utils.db_connection import engine


def read_db(table: str, columns: list[str]):
    df = pd.read_sql_table(table_name=table, con=engine.connect(), columns=columns)
    return df


def upload_df_into_db():
    pass



colmns = ['id', 'order_date']
tbl = 'Purchase'

print(read_db(tbl, colmns))