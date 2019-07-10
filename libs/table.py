"""
Библиотека хелперов
"""
from math import ceil
from csv import DictWriter, DictReader

from libs.data import DataTransaction


class TableCSV:
    data = DataTransaction
    file_name = 'data.csv'

    # Функция для генерации таблицы csv
    def create_table_csv(self):
        with open(self.file_name, 'w') as csvfile:
            writer = DictWriter(csvfile, fieldnames=self.data.columns)
            writer.writeheader()

            for cur_dict in self.data.rows:
                writer.writerow(cur_dict)

    # Функция для получения таблицы из csv таблицы
    def load_table_csv(self):
        data = []
        try:
            with open(self.file_name, 'r') as file:
                reader = DictReader(file, delimiter=',')
                for line in reader:
                    data.append(dict(line))
                for dt in data:
                    dt['Netto'] = int(dt.get('Netto'))
                    dt['VAT rate'] = int(dt.get('VAT rate'))
                    dt['VAT sum'] = ceil(float(dt.get('VAT sum')))
            return data
        except FileNotFoundError:
            return []