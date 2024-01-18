# 2) користувач вводить числа a, b  вивиести всі цілі числа муж ними
import math

num_a = float(input("Введіть число A: "))
num_b = float(input("Введіть число B, де B > A: "))
list_1 = [num_a,num_b]
print(list_1)

for i in range(math.ceil(num_a), math.floor(num_b)):
    if i not in list_1:
      print(i)