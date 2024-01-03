"""
№2 задачку з файлу task_from_hw.py переписати з використанням рекурсії
В нас є кількість грошей та каса з купюрами.
Відпости чи зможемо ми видати цю сумму тими купюрами що в нас є
currency = {100:2, 50:10, 20:0, 10:0, 5:100, 2:10, 1:10}
"""

def recursive_check_curr(kasa, amount):
    #print(f'Amount: {amount}, kasa: {kasa}')  # Додали друк для відстеження
    if len(kasa) == 0:
        return amount == 0
    key = next(iter(kasa))  # Отримуємо перший ключ словника
    max_amount = amount // key
    if max_amount > kasa[key]:
        amount -= key * kasa[key]
    else:
        amount -= key * max_amount
    del kasa[key]  # Видаляємо ключ, який ми обробили
    return recursive_check_curr(kasa, amount)

# Приклади використання
assert recursive_check_curr({100: 2, 1: 10}, 211) == False
assert recursive_check_curr({100: 2, 2: 10}, 201) == False
assert recursive_check_curr({100:2, 1:10}, 57) == False
assert recursive_check_curr({100: 2, 5: 8, 1: 10}, 57) == False
assert recursive_check_curr({100: 2, 50: 1, 1: 10}, 157) == True
assert recursive_check_curr({100: 0, 50: 10, 5: 10, 1: 10}, 327) == True
assert recursive_check_curr({500:1, 100:2, 1:10}, 200) == True

def iter_check_curr(kasa, amount):
    for key in kasa.keys(): #Перебираємо всі ключі у словнику kasa
        max_amount = amount // key #Для кожного номіналу купюри обчислюємо максимальну кількість купюр
        tmp = kasa[key]
        if max_amount > kasa[key]:
            #Якщо max_amount > за кількість купюр, які є в касі, то зменшуємо на суму грошей, які взяли з каси
            amount = amount - key * kasa[key] #kasa[key] - кількість купюр номіналу key що є в касі
        else:
            amount = amount - max_amount * key
    if amount != 0:
        return False
    return True

assert iter_check_curr({100: 2, 1: 10}, 211) == False
assert iter_check_curr({100: 2, 2: 10}, 201) == False
assert iter_check_curr({100:2, 1:10}, 57) == False
assert iter_check_curr({100: 2, 5: 8, 1: 10}, 57) == False
assert iter_check_curr({100: 2, 50: 1, 1: 10}, 157) == True
assert iter_check_curr({100: 0, 50: 10, 5: 10, 1: 10}, 327) == True
assert iter_check_curr({500:1, 100:2, 1:10}, 200) == True

