# 3) Вивести всі числа між числами a, b , 1 < (a,b) < 200 що діляться на 2, 3, 4, 5, 6.
# Кожна группа має бути виведена окремою групою, зі строкою не більше 10 чисел
# output example:
# Dividible by 2: 2,  4, 6,  8, 10, 12, 14, 16, 18, 20,
#                 22, 24, 26
# Dividible by 3: .......

def divided_numbers(divisor, lst):
    counter = 0
    print(f"Числа, які діляться на {divisor}:")
    for i in range(min(lst), max(lst) + 1):
        if i % divisor == 0:
            print(f"{i:3}", end=" ")
            counter += 1
            if counter == 10:  # Якщо досягнуто 10 чисел у рядку, перехід на новий рядок
                print()
                counter = 0  # Скидання лічильника для наступної групи чисел
    print("\n")

list1 = [1, 200]
divisors = [2, 3, 4, 5, 6]

for divisor in divisors:
    divided_numbers(divisor, list1)
