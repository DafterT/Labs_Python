# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, spliter=','):
    set_intersection = set(str1.split(spliter)).intersection(str2.split(spliter))
    return sorted(list(set_intersection))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, spliter='|')
