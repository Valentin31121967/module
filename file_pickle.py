# Обращаемся к файлу user1.py для использования переменной ser_user
from user1 import ser_user
import pickle
# Функция сохранения данных в формате pickle  в файл fil
def user_pickle_dumps():
    fil = input("Введите с клавиатуры имя файла, в который нужно записать данные:  ")
    pickle_dumps_user = pickle.dumps(ser_user)
    with open(fil, 'wb') as f:
        f.write(pickle_dumps_user)
    print(pickle_dumps_user)
user_pickle_dumps()
# Функция загрузки данных из файла fil в формате pickle
def user_pickle_loads():
    fil = input("Введите с клавиатуры имя файла, с которого нужно загрузить данные:  ")
    d = {}
    with open(fil, "rb") as f:
        pickle_loads_user = f.read()
    print(type(pickle_loads_user))
    d = pickle.loads(pickle_loads_user)
    print(type(d))
    print(d)
user_pickle_loads()
