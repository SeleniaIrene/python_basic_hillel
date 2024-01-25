# Завдання 5
# Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.

def find_common_elements(input_list1: str, input_list2: str) -> list:

    try:
        numbers_str = input_list1.split(',')
        list_1 = [int(num.strip()) for num in numbers_str]
        numbers_str = input_list2.split(',')
        list_2 = [int(num.strip()) for num in numbers_str]
    except ValueError:
        print("Помилка при перетворенні введення у список цілих чисел.")
        return None

    set_list_1 = set(list_1)
    set_list_2 = set(list_2)
    common_elements = set_list_1.intersection(set_list_2)

    return list(common_elements) if list_1 and list_2 and common_elements else None

user_input_list1 = input("Введіть список цілих чисел через кому: ")
user_input_list2 = input("Введіть список цілих чисел через кому: ")

result = find_common_elements(user_input_list1, user_input_list2)
print(f"Елементи, що містяться в обох списках: {result}")

# Тести
assert find_common_elements("1, 2, 3, 4, 5", "3, 4, 5, 6, 7") == [3, 4, 5]
assert find_common_elements("10, 20, 30", "20, 30, 40") == [20, 30]
assert find_common_elements("1, 2, 3", "4, 5, 6") == None
assert find_common_elements("1, two, 3", "4, 5, 6") == None
assert find_common_elements("", "4, 5, 6") == None

