import pandas as pd
from django.core.management.base import BaseCommand
from datatransfer.models import Purchase
from sqlalchemy import create_engine
from colorama import Fore


class Command(BaseCommand):
    help = "Выгружает данные датафрейма в БД"

    def handle(self, *args, **options):

        file = "csv_files/purchase_data.csv"
        df = pd.read_csv(file)

        url = "postgresql://postgres:ElonMusk@localhost:5433/data_api"
        engine = create_engine(url)

        try:
            df.to_sql(Purchase._meta.db_table, if_exists='replace', con=engine, index=True)
            self.stdout.write(Fore.GREEN + "\nВыгрузка данных завершена.")
        except Exception:
            raise Exception(Fore.RED + "Ошибка")