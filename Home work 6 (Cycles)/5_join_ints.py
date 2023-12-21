"""
Із списку, цілі числа з'єднати в одне число
варіант із зірочкою - заборонено переведення із строкового в числовий тип і навпаки
"""

def join_ints(my_list):
    stringified = ''
    result = ''
    for i in my_list:
        if isinstance(i, int):
            stringified = str(i)
            result += stringified
    return(int(result))

assert join_ints([1, 2, 3]) == 123
assert join_ints([1, "foo", 2.5, 1, 1, 4, "abr", 3]) == 11143
