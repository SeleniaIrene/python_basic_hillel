# Завдання 1.
# Написати рекурсивну функцію знаходження ступеня числа.

def get_number_pow(number_input: int, pow_input: int) -> int:
    try:
        number = int(number_input)
        number_pow = int(pow_input)
    except ValueError:
        print("Помилка: Введіть коректне ціле число.")
        return None

    if number_pow <= 0:
        number_in_pow = 1
    elif number_pow == 1:
        number_in_pow = number
    else:
        number_in_pow = number * get_number_pow(number, number_pow - 1)

    return number_in_pow if number is not None and number_pow is not None else None

user_number = input("Введіть ціле число: ")
user_pow = input("Введіть ступінь, в яку ви хочете возвести число: ")

result = get_number_pow(user_number, user_pow)
print(f"Нове число: {result}")

#Тести
assert get_number_pow(2, 3) == 8
assert get_number_pow(5, 0) == 1
assert get_number_pow(3, -2) == 1
assert get_number_pow(2, 1) == 2
assert get_number_pow(0, 0) == 1
assert get_number_pow('abc', 2) is None
assert get_number_pow(5, "") is None

