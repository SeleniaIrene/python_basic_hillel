# Завдання 3
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

def looking_prime_numbers(user_input: str) -> list:
    prime_numbers_list = []

    try:
        numbers_str = user_input.split(',')
        numbers_list = [int(num.strip()) for num in numbers_str]
    except ValueError:
        print("Помилка при перетворенні введення у список цілих чисел.")
        return None

    if all(num == 0 or num == 1 for num in numbers_list):
        return None

    for num in numbers_list:

        if num < 2:
           continue

        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
           prime_numbers_list.append(num)

    return prime_numbers_list if numbers_list else None

user_list = input("Введіть список цілих чисел через кому: ")

result = looking_prime_numbers(user_list)

if result is not None:
    print(result)
else:
    print("Функція не вдалася через помилку вводу.")

# Тести
assert looking_prime_numbers("2,3,5,7,11") == [2, 3, 5, 7, 11]
assert looking_prime_numbers("1,4,6,8,9,10,13,17,19,23,29") == [13, 17, 19, 23, 29]
assert looking_prime_numbers("") == None
assert looking_prime_numbers("1111б222,22,333,55,11,888,444,00,323,056,02") == None

