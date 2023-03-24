import pandas as pd
from django.core.management.base import BaseCommand
from datatransfer.models import Purchase
from datatransfer.services.db_connection import engine
from colorama import Fore


class Command(BaseCommand):
    help = "Выгружает данные датафрейма в БД"

    def handle(self, *args, **options):
        data = options['file']
        # file = "csv_files/purchase_data.csv"
        df = pd.read_csv(data)
        try:
            df.to_sql(
                Purchase._meta.db_table,
                if_exists='replace',
                con=engine, index=True,
                index_label='id'
            )
            self.stdout.write(Fore.GREEN + "\nВыгрузка данных завершена.")
        except Exception:
            raise Exception(Fore.RED + "Ошибка")

    def add_arguments(self, parser):
        parser.add_argument('file')
