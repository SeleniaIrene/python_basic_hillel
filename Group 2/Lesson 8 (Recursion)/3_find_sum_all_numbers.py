# Завдання 3.
# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.

def find_sum_all_numbers(input_number1: int, input_number2: int) -> int:
    try:
        number_1 = int(input_number1)
        number_2 = int(input_number2)
    except ValueError:
        print("Помилка: Введіть коректне ціле число.")
        return None

    if number_1 > number_2:
        (number_1, number_2) = (number_2, number_1)

    if number_1 >= number_2:
        return number_1
    else:
        result_sum = number_1 + find_sum_all_numbers(number_1 + 1, number_2)

    return result_sum

user_number_1 = input("Введіть ціле число: ")
user_number_2 = input("Введіть ціле число: ")
print(f"Сумма між числами {user_number_1,user_number_2} дорівнює {find_sum_all_numbers(user_number_1,user_number_2)}")

#Тести
assert find_sum_all_numbers(5,1) == 15
assert find_sum_all_numbers(0,5) == 15
assert find_sum_all_numbers(0,1) == 1
assert find_sum_all_numbers(-1,1) == 0
assert find_sum_all_numbers("",1) == None
assert find_sum_all_numbers(0,"fmg") == None
