# Множини, списки, рядки:
# 1. Створити список чисел. Заберіть дублікати значень. Вивести унікальні значення.
numbers = [1, 2, 3, 4, 5, 3, 4, 5, 5]
set_numbers_list = list(set(numbers))
print(set_numbers_list)

unique_numbers_list = []
for num in numbers:
    if num not in unique_numbers_list:
        unique_numbers_list.append(num)
print(unique_numbers_list)
