print("----------------------------------- 0 -----------------------------------")
# 0) Пользователь воодит пароль - ми кажемо чи беспечний цей пароль чи ні.
# Пароль беспечний, якщо він довший за 12 символів.
# Має 1 букву в верхньому регистрі, 1 в нижньому, 1 цифру, 1 спецсимвол(?/!@)
password = input("Введіть пароль, що відповідає вимогам: ")

if len(password) <= 12:
    print("Пароль не безпечний: недостатня довжина")
if not any(char.isupper() for char in password):
    print("Пароль не безпечний: відсутня буква в верхньому регістрі")
if not any(char.islower() for char in password):
    print("Пароль не безпечний: відсутня буква в нижньому регістрі")
if not any(char.isdigit() for char in password):
    print("Пароль не безпечний: відсутні цифри")
if not any(char in ('?', '/', '!', '@') for char in password):
    print("Пароль не безпечний: відсутній спецсимвол")
else:
    print(f"Пароль безпечний. Ваш пароль: {password}")

print("\n")
print("----------------------------------- 1 -----------------------------------")
# 1) У нескінченному циклі користувач вводить числа.
#  Коли ви пишете слово end цикл припиняється і програма видає сумму числел.
total = 0

while True:
    user_input = input("Введіть число або 'end' для завершення: ")
    if user_input.lower() == 'end':
        break
    if not user_input.isdigit():
        user_input = int(0)
    total = total + int(user_input)
print(f"Сума введених чисел: {total}")

print("\n")
print("----------------------------------- 2 -----------------------------------")
# 2) користувач вводить числа a, b  вивиести всі цілі числа муж ними
import math

num_a = float(input("Введіть число A: "))
num_b = float(input("Введіть число B, де B > A: "))
list_1 = [num_a,num_b]
print(list_1)

for i in range(math.ceil(num_a), math.floor(num_b)):
    if i not in list_1:
      print(i)

print("\n")
print("----------------------------------- 3 -----------------------------------")
# 3) Вивести всі числа між числами a, b , 1 < (a,b) < 200 що діляться на 2, 3, 4, 5, 6.
# Кожна группа має бути виведена окремою групою, зі строкою не більше 10 чисел

# output example:
# Dividible by 2: 2 ,  4,  6,  8, 10, 12, 14, 16, 18, 20,
#                 22, 24, 26
# Dividible by 3: .......

list_2 = [1, 200]
counter = 0

print("Числа, які діляться на 2:")
for i in range(min(list_2), max(list_2) + 1):
    if i % 2 == 0:
        print(f"{i:3}", end=" ")
        counter += 1
        if counter == 10:  # Якщо досягнуто 10 чисел у рядку, перехід на новий рядок
            print()
            counter = 0

counter = 0
print("\nЧисла, які діляться на 3:")
for i in range(min(list_2), max(list_2) + 1):
    if i % 3 == 0:
        print(f"{i:3}", end=" ")
        counter += 1
        if counter == 10:  # Якщо досягнуто 10 чисел у рядку, перехід на новий рядок
            print()
            counter = 0

counter = 0
print("\nЧисла, які діляться на 4:")
for i in range(min(list_2), max(list_2) + 1):
    if i % 4 == 0:
        print(f"{i:3}", end=" ")
        counter += 1
        if counter == 10:  # Якщо досягнуто 10 чисел у рядку, перехід на новий рядок
            print()
            counter = 0

counter = 0
print("\nЧисла, які діляться на 5:")
for i in range(min(list_2), max(list_2) + 1):
    if i % 5 == 0:
        print(f"{i:3}", end=" ")
        counter += 1
        if counter == 10:  # Якщо досягнуто 10 чисел у рядку, перехід на новий рядок
            print()
            counter = 0

counter = 0
print("\nЧисла, які діляться на 6:")
for i in range(min(list_2), max(list_2) + 1):
    if i % 6 == 0:
        print(f"{i:3}", end=" ")
        counter += 1
        if counter == 10:  # Якщо досягнуто 10 чисел у рядку, перехід на новий рядок
            print()
            counter = 0

print("\n")
print("----------------------------------- 4 -----------------------------------")
# 4) Користувач вводить число від 1 до 100. Вивести таблицю множення на це число
# 4*) Користувач вводить число від 6 до 16. Вивести таблицю множення на числа від n - 4  до n + 3(Як на зошитах).

#  В d випадку з 6 від 2 до 9. 16 - від 12 до 19
#  output:
#  2 * 2 = 4  3 * 2 = 6 4 * 2 = 8  .........
#  2 * 3 = 6  3 * 3 = 9 4 * 3 = 12 .........

user_number = int(input("Введіть число від 6 до 16: "))

if 6 <= user_number <= 16:
    start = user_number - 4
    end = user_number + 3

    for i in range(start, end + 1):
        for j in range(1, 11):
            print(f"{i: 2} * {j: 2} = {i * j: 3}")
        print("\n")  # Перехід на новий рядок після кожного числа таблиці
else:
    print("Введене число не входить в діапазон від 6 до 16")
