# Завдання 6
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список також передається як параметр.
# Функція повертає новий список, який містить отримані результати.

def raise_number_to_power(list_input: list, number_input: int) -> list:
    result_list = []

    try:
        numbers_str = list_input.split(',')
        numbers_list = [int(num.strip()) for num in numbers_str]
    except ValueError:
        print("Помилка при перетворенні введення у список цілих чисел.")
        return None

    try:
        exponent = int(number_input)
    except ValueError:
        print("Помилка: Введіть коректне ціле число.")
        return None

    for num in numbers_list:

        if exponent == 1:
            number_in_pow = num
        elif exponent <= 0:
            number_in_pow = 1
        else:
            number_in_pow = pow(num, exponent)
        result_list.append(number_in_pow)

    return list(result_list) if numbers_list and exponent is not None else None

user_list = input("Введіть список цілих чисел через кому: ")
user_number = input("Ступінь, в яку ви хочете возвести числа: ")

result = raise_number_to_power(user_list, user_number)
print(f"Новий список: {result}")

# Тести
assert raise_number_to_power("2,3,4", 2) == [4, 9, 16]
assert raise_number_to_power("5,6,7", 3) == [125, 216, 343]
assert raise_number_to_power("1,2,3", 0) == [1, 1, 1]
assert raise_number_to_power("2,4,6", -1) == [1, 1, 1]
assert raise_number_to_power("2,3,4", 1) == [2, 3, 4]
assert raise_number_to_power("", 2) == None
assert raise_number_to_power("7,8,9", "") == None
assert raise_number_to_power("2,abc,4", 2) == None
assert raise_number_to_power("2,3,4", "abc") == None
