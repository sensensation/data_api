import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
django.setup()

import sys
import pandas as pd
from colorama import Fore
from datatransfer.models import Purchase
from db_connection import engine


def read_db(table: str, columns: list[str]):
    df = pd.read_sql_table(table_name=table, con=engine.connect(), columns=columns)
    return df


def save_to_db(df):
    try:
        df.to_sql(
            Purchase._meta.db_table,
            if_exists='replace',
            con=engine, index=True,
            index_label='id'
        )
        return sys.stdout.write(Fore.GREEN + "\nОбновление данных завершено.")
    except Exception:
        raise Exception(Fore.RED + "Ошибка")


def refactor_date(df, series):
    df[series] = pd.to_datetime(df[series])

    try:
        df.to_csv(
            'out.csv', index=False
        )
    except Exception:
        raise Exception


colmns = ['order_id', 'product',
          'quantity_ordered', 'order_date',
          'price_each', 'purchase_adress',
          'total']

tbl = 'Purchase'

df1 = read_db(tbl, colmns)

refactor_date(df1, "order_date")


