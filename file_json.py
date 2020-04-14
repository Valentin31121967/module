# Обращаемся к файлу user1.py для использования переменной ser_user
from user1 import ser_user
import json
# Функция сохранения данных в формате json  в файл fil
def user_json_dumps():
    fil = input("Введите с клавиатуры имя файла, в который нужно записать данные:  ")
    json_dumps_user = json.dumps(ser_user)
    with open(fil, 'w') as f:
        f.write(json_dumps_user)
    print(json_dumps_user)
user_json_dumps()
# Функция загрузки данных из файла fil в формате json
def user_json_loads():
    fil = input("Введите с клавиатуры имя файла, с которого нужно загрузить данные:  ")
    d = {}
    with open(fil, "r") as f:
        json_loads_user = f.read()
    print(type(json_loads_user))
    d = json.loads(json_loads_user)
    print(type(d))
    print(d)
user_json_loads()