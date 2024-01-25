# Завдання 1
# Напишіть функцію, яка обчислює добуток елементів списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

def list_items_multiplication(user_input: str) -> int:
    numbers_list = []
    multiplicate_num = 1

    try:
        numbers_str = user_input.split(',')
        numbers_list = [int(num.strip()) for num in numbers_str]
    except ValueError:
        print("Помилка при перетворенні введення у список цілих чисел.")

    for num in numbers_list:
        multiplicate_num *= num

    return multiplicate_num if numbers_list else None

user_list = input("Введіть список цілих чисел через кому: ")

result = list_items_multiplication(user_list)

if result is not None:
    print(result)
else:
    print("Функція не вдалася через помилку вводу.")

# Тести
assert list_items_multiplication("2, 3, 4, 5") == 120
assert list_items_multiplication("-2, 3, 4, 5") == -120
assert list_items_multiplication("0, 1, 2, 3") == 0
assert list_items_multiplication("42") == 42
assert list_items_multiplication("") == None
assert list_items_multiplication("не ціле число, 2, 3") == None
