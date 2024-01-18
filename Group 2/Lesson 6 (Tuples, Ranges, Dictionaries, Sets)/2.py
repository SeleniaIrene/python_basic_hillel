# 2. Дано два списки чисел.
# Порахуйте, скільки унiкальних чисел міститься як у першому списку, і у другому.

first_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
second_list = [4, 5, 6, 7, 8, 4, 5, 6, 7, 8]

unique_in_first = set(first_list)
unique_in_second = set(second_list)

difference_first_second = unique_in_first.difference(unique_in_second)
difference_second_first = unique_in_second.difference(unique_in_first)

print("Унікальні числа в першому списку:", len(unique_in_first))
print("Унікальні числа в другому списку:", len(unique_in_second))
print("Унікальні числа в першому списку, але не в другому:", difference_first_second)
print("Унікальні числа в другому списку, але не в першому:", difference_second_first)
