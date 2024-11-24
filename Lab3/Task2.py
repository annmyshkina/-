# TODO Напишите функцию find_common_participants
def find_common_participants(group_first, group_second, split_str=","):
    first_group = set(group_first.split(split_str))
    second_group = group_second.split(split_str)
    set_result = first_group.intersection(second_group)
    common_participants = []
    for i in set_result:
        common_participants.append(i)
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, "|"))
# TODO Провеьте работу функции с разделителем отличным от запятой
