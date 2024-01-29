# Завдання 4.
# Напишіть рекурсивну функцію, яка приймає одновимірний масив із 100 цілих чисел
# заповнених випадковим чином і знаходить позицію,
# з якої починається послідовність із 10 чисел, сума яких мінімальна.

def find_min_sum_position(arr, current_position=0, min_position=0, min_sum=float('inf')):
    # Функція приймає масив arr та встановлює значення за замовчуванням для поточної позиції,
    # позиції з мінімальною сумою та мінімальної суми.

    if current_position > len(arr) - 2:
        # Якщо поточна позиція виходить за межі масиву (останній елемент чи вище),
        # то повертаємо позицію з мінімальною сумою.

        return min_position

    current_sum = arr[current_position] + arr[current_position + 1]
    # Обчислюємо суму двох послідовних чисел, починаючи з поточної позиції.

    if current_sum < min_sum:
        # Якщо поточна сума менша за мінімальну суму, то оновлюємо значення
        # мінімальної суми та позиції.

        min_sum = current_sum
        min_position = current_position

    return find_min_sum_position(arr, current_position + 1, min_position, min_sum)
    # Рекурсивний виклик для наступної позиції.

# Приклад використання:
import random

random_array = [random.randint(1, 100) for _ in range(10)]
# Згенеруємо випадковий масив з 10 цілих чисел.

print("Згенерований масив:", random_array)

min_sum_position = find_min_sum_position(random_array)
print("Позиція, з якої починається послідовність із 2 чисел, сума яких мінімальна:", min_sum_position)
# Виведення результату роботи функції.
