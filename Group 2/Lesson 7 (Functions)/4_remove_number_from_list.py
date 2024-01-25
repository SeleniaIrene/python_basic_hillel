# Завдання 4
# Напишіть функцію, яка видаляє зі списку ціле задане число.
# З функції потрібно повернути кількість видаленних елементів.

numbers_list = [1, 2, 6, 5, 3, 4, 8, 3, 5, 5, 3, 7, 9, 6]
print(f"Заданий список: {numbers_list}")

def remove_number_from_list(numbers_list: list, user_input: int) -> list:

    try:
        number_to_remove = int(user_input)
    except ValueError:
        print("Помилка: Введіть коректне ціле число.")
        return None

    if number_to_remove in numbers_list:
        while number_to_remove in numbers_list:
            numbers_list.remove(number_to_remove)
    else:
        print(f"Число {number_to_remove} не знайдено у списку.")
        return None

    print(f"Число {number_to_remove} видалено. Новий список: {numbers_list}")
    return numbers_list if number_to_remove else None

user_number = input("Введіть число зі списку, яке ви хочете видалити: ")

result = remove_number_from_list(numbers_list, user_number)

# Тести
assert remove_number_from_list(numbers_list, "3") == [1, 2, 6, 5, 4, 8, 5, 5, 7, 9, 6]
assert remove_number_from_list(numbers_list, "-1") == None
assert remove_number_from_list(numbers_list, "abc") == None
assert remove_number_from_list(numbers_list, "0") == None
assert remove_number_from_list([], "3") == None
