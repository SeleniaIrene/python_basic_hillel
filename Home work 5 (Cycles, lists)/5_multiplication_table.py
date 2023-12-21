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