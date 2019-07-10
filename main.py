"""
Скрипт для запуска всего процесса:
1) Формирование csv таблицы
2) Подсчёт ндс и вывод сообщений
"""

from libs.table import TableCSV
from libs.report import Report

if __name__ == '__main__':

    res = ''
    table = TableCSV()
    report = Report

    # Генерация csv файла
    table.create_table_csv()

    # извлечение данных
    data = table.load_table_csv()

    # Проверка данных
    if not data:
        res += 'Нету данных для отчёта'
        print(res)

    # Получение невалидного рассчёта НДС
    messages = report.get_transaction_novalid_nds(data)

    if messages:
        for msg in messages:
            res = 'Описание продажи: ' + msg.get('Description') + '\n' + \
                   'Сумма Нетто: ' + str(msg.get('Netto')) + '\n' + \
                   'Страна: ' + msg.get('Delivery country') + '\n' + \
                   'Ставка НДС: ' + str(msg.get('VAT rate')) + '\n' + \
                   'Сумма НДС: ' + str(msg.get('VAT sum')) + '\n\n'
            print(res)
        print('Конец отчёта')


