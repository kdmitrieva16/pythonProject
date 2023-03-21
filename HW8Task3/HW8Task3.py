"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml

items = [
    'computer',
    'printer',
    'keyboard',
    'mouse'
]

items_quantity = 4
items_price = {
    'computer':  str(300) + u'\u20AC',
    'printer': str(200) + u'\u20AC',
    'keyboard': str(100) + u'\u20AC',
    'mouse': str(50) + u'\u20AC',

}

data_to_yaml = {'items': items, 'items_quantity': items_quantity, 'items_price': items_price}

with open('test.yaml', 'w', encoding='utf-16') as out_file:
    yaml.dump(data_to_yaml, out_file, allow_unicode=True, default_flow_style=False)

with open('test.yaml', 'r', encoding='utf-16') as file_read:
    print(yaml.safe_load(file_read) == data_to_yaml)