# непарная кількість
# my_list = [1, 2, 3, 4, 5]
# my_list_len = len(my_list)
#
# if my_list_len % 2 == 0:
#     first_part = my_list[:my_list_len // 2]
#     second_part = my_list[my_list_len // 2:]
#     result_list = [first_part, second_part]
# else:
#     second_part = my_list[(my_list_len // 2) + 1:]
#     first_part = my_list[:(my_list_len // 2) + 1]
#     result_list = [first_part, second_part]
#
# print(result_list)

# Парна
# my_list = [1, 2, 3, 4, 5, 6]
# my_list_len = len(my_list)
#
# if my_list_len % 2 == 0:
#     first_part = my_list[:my_list_len // 2]
#     second_part = my_list[my_list_len // 2:]
#     result_list = [first_part, second_part]
# else:
#     second_part = my_list[(my_list_len // 2) + 1:]
#     first_part = my_list[:(my_list_len // 2) + 1]
#     result_list = [first_part, second_part]
# 
#
# print(result_list)

# нуль
my_list = []
my_list_len = len(my_list)

if my_list_len % 2 == 0:
    first_part = my_list[:my_list_len // 2]
    second_part = my_list[my_list_len // 2:]
    result_list = [first_part, second_part]
else:
    second_part = my_list[(my_list_len // 2) + 1:]
    first_part = my_list[:(my_list_len // 2) + 1]
    result_list = [first_part, second_part]


print(result_list)
