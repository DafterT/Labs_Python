list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
number_of_players_in_one_team = len(list_players) // 2

first_team = list_players[:number_of_players_in_one_team]
second_team = list_players[number_of_players_in_one_team:]
print(first_team, second_team, sep='\n')
