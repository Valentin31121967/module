# Функция создания модуля user1
def input_user():
    data_user = {}
    data_user["number"] = int(input("Введите номер по списку"))
    data_user["first_name"] = str(input("Введите Фамилию: "))
    data_user["middle_name"] = str(input("Введите Имя: "))
    data_user["last_name"] = str(input("Введите  Отчество: "))
    data_user["age"] = int(input("Введите возраст: "))
    return data_user
user1 = input_user()
# Функция сериализации данных словаря в строку для вывода на экран
def serialize(user1):
    res = "Number : {}\n"\
        "First name : {}\n" \
          "Middle name : {}\n" \
          "Last name : {}\n" \
          "Age        : {}".format(user1["number"],
                                   user1["first_name"],
                                   user1["middle_name"],
                                   user1["last_name"],
                                   user1["age"])
    return res
ser_user = serialize(user1)
print(ser_user)
