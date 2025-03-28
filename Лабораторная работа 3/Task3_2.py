# TODO Напишите функцию find_common_participants
def find_common_participants(string1, string2, spliter=','):
    names_list = sorted(list(set(string1.split(spliter)) & (set(string2.split(spliter)))))
    return names_list



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
spl = '|'
print(find_common_participants(participants_first_group, participants_second_group, spl))
# TODO Проверьте работу функции с разделителем отличным от запятой
