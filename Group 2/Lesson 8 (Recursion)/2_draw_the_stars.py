# Завдання 2.
# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)

def draw_the_stars(number_input: int) -> int:
    try:
        number_stars = int(number_input)
    except ValueError:
        print("Помилка: Введіть коректне ціле число.")
        return 0

    if number_stars <= 0:
        return 0
    else:
        print("*" * number_stars)
        return 1 + draw_the_stars(number_stars - 1)

user_number = input("Введіть ціле число: ")
draw_the_stars(user_number)

#Тести
assert draw_the_stars("") == 0
assert draw_the_stars(-5) == 0
assert draw_the_stars(0) == 0
assert draw_the_stars(1) == 1
assert draw_the_stars(5) == 5