users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
users_dict = {
    "Общее количество" : 0,
    "Уникальные посещения" : 0
}

users_dict["Общее количество"] = len(users)
users_dict["Уникальные посещения"] = len(set(users))

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
print(users_dict)