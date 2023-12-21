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
