# Обращаемся к файлу user1.py для использования данных из этого файла  для работы
from user1 import user1
# Функция  получения списка пользователей для работы users, используя модуль user1
def update1_user():
    user2 = {}
    user_update = []
    user_update.append(user1)
    print(user1)
    yes_user = int(input("Если  хотите добавить пользователя нажмите - 1"))
    if yes_user == 1:
        for key in user1:
            if key == "number":
                number = int(input("Номер по списку: "))
                user2["number"] = number
            if key == "first_name":
                first_name = str(input("Фамилию: "))
                user2["first_name"] = first_name
            if key == "middle_name":
                middle_name = str(input("Имя: "))
                user2["middle_name"] = middle_name
            if key == "last_name":
                last_name = str(input("Отчество: "))
                user2["last_name"] = last_name
            if key == "age":
                age = int(input("Возраст: "))
                user2["age"] = age
        print(user2)
        user_update.append(user2)
    return user_update
users = update1_user()
print(users)
# Функция записи данных в файл
import json
def user_json_save(users):
    fil = input("Введите с клавиатуры имя файла, в который нужно записать данные:  ")
    json_dumps_user = json.dumps(users)
    with open(fil, 'w') as f:
        f.write(json_dumps_user)
    print(json_dumps_user)
user_json_save(users)
# Функция загрузки данных списка пользователей из файла
def user_json_loads():
    fil = input("Введите с клавиатуры имя файла, с которого нужно загрузить данные:  ")
    users = []
    with open(fil, "r") as f:
        json_loads_user = f.read()
        users = json.loads(json_loads_user)
    print(type(users))
    print(users)
    return users
user_json_loads()
# Функция удаления пользователя по имени из списка пользователей
def user_del():
    print(users)
    user_app = "true"
    while user_app == "true":
        user_del = input("Введите  имя пользователя, которого нужно удалить")
        f = 0
        for user in users:
            print(user)
            for value in user.values():
                if value == user_del:
                    f = user_del
                    users.remove(user)
        if f == 0:
            print("Таких данных пользователя  нет в этом списке")
        k = int(input("Чтобы остаться в режиме удаления пользователя, нажмите 1"))
        if k == 1:
            user_app = "true"
        else:
            user_app = "false"
    return users
n = user_del()
print(n)
user_json_save(users)
user_json_loads()
# Функция добавления пользователя к уже существующему списку пользователей users
def update2_user():
    print(users)
    user_app = "true"
    while user_app == "true":
        yes_user = int(input("Если  хотите добавить пользователя нажмите - 1"))
        if yes_user == 1:
            number = int(input('Введите номер пользователя'))
            first_name = str(input('Введите фамилию пользователя'))
            middle_name = str(input('Введите имя пользователя'))
            last_name = str(input('Введите отчество пользователя'))
            age = int(input('Введите возраст пользователя'))
            user = {"number": number, "first_name": first_name, "middle_name": middle_name, "last_name": last_name, "age": age}
            print(user)
            print(users.append(user))
        k = int(input("Чтобы остаться в режиме добавления  пользователя, нажмите 1"))
        if k == 1:
            user_app = "true"
        else:
            user_app = "false"
    return users
update2_user()
print(users)
user_json_save(users)
user_json_loads()
# Удаление пользователей по номеру из списка пользователей
def user_del():
    print(users)
    user_app = "true"
    while user_app == "true":
        user_del = int(input("Введите  номер пользователя, которого нужно удалить"))
        f = 0
        for user in users:
            for value in user.values():
                if value == user_del:
                    f = user_del
                    users.remove(user)
        if f == 0:
            print("Таких данных пользователя  нет в этом списке")
        k = int(input("Чтобы остаться в режиме удаления пользователя, нажмите 1"))
        if k == 1:
            user_app = "true"
        else:
            user_app = "false"
    return users
n = user_del()
print(n)
# Функция обновления данных пользователя по номеру
user_json_save(users)
user_json_loads()
def update_number():
    print(users)
    user_app = "true"
    while user_app == "true":
        user_update = int(input("Если хотите обновить данные у пользователя, нажмите 1"))
        user_number = int(input("Введите  номер пользователя, у которого нужно обновить данные "))
        user_means = str(input("Введите, что нужно обновить (first_name, middle_name, last_name)"))
        user_age = input("Если нужно обновить возраст, наберите название age")
        if user_update == 1:
            for user in users:
                if user["number"] == user_number:
                    for key in user:
                        if key == user_means:
                            user_key_means = input("Введите новое название для   " + user_means + "  .")
                            user[user_means] = user_key_means
                        if key == user_age:
                            user_key_age = int(input("Введите " + user_age + "  для обновления"))
                            user[user_age] = user_key_age
        k = int(input("Чтобы остаться в режиме обновления данных пользователя, нажмите 1"))
        if k == 1:
            user_app = "true"
        else:
            user_app = "false"
    return users
update_number()
print(users)

# Функция обновления данных пользователя по имени
user_json_save(users)
user_json_loads()
def update_number():
    print(users)
    user_update = int(input("Если хотите обновить данные у пользователя, нажмите 1"))
    user_name = str(input("Введите  имя пользователя, у которого нужно обновить данные "))
    user_means = str(input("Введите, что нужно обновить (first_name, middle_name, last_name)"))
    user_age = input("Если нужно обновить возраст, наберите название age")
    if user_update == 1:
        for user in users:
            if user["middle_name"] == user_name:
                for key in user:
                    if key == user_means:
                        user_key_means = input("Введите новое название для  " + user_means + ".")
                        user[user_means] = user_key_means
                    if key == user_age:
                        user_key_age = int(input("Введите " + user_age + "  для обновления"))
                        user[user_age] = user_key_age
        else:
            print("Обновите в следующий раз")
    return users
update_number()
print(users)
user_json_save(users)




