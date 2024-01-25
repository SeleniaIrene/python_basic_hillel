# Завдання 2
# Напишіть функцію для знаходження мінімуму у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

def list_find_minimum(user_input: str) -> int:
    numbers_list = []

    try:
        numbers_str = user_input.split(',')
        numbers_list = [int(num.strip()) for num in numbers_str]
    except ValueError:
        print("Помилка при перетворенні введення у список цілих чисел.")

    if not numbers_list:
        return None

    min_num = numbers_list[0]
    for num in numbers_list:
        if num < min_num:
            min_num = num

    return min_num

user_list = input("Введіть список цілих чисел через кому: ")

result = list_find_minimum(user_list)

if result is not None:
    print(result)
else:
    print("Функція не вдалася через помилку вводу.")

# Тести
assert list_find_minimum("3, 1, 8, 4, 6") == 1
assert list_find_minimum("0, 1, 0, 1, 0, 1") == 0
assert list_find_minimum("-10, -5, 8, -3, 0") == -10
assert list_find_minimum("42") == 42
assert list_find_minimum("") == None
assert list_find_minimum("не ціле число, 2, 3") == None
