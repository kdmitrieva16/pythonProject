"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра. """
import json


def write_order_to_json(item, quantity, price, buyer, date):
    order_data = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }
    with open('orders.json', 'w', encoding='cp1251') as write_json:
        json.dump(order_data, write_json, indent=4, ensure_ascii=False)


write_order_to_json(
    item=['молоко', 'хлеб', 'масло'],
    quantity=[2, 3, 1],
    price=[87.00, 50.00, 169.50],
    buyer=['Иванов Иван'],
    date=['20.03.23'])
