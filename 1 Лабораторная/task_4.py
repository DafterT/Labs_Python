users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dir_ = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
dir_['Общее количество'] = len(users)
dir_['Уникальные посещения'] = len(set(users))

print(dir_)
