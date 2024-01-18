"""
Реалізувати метод строк split() самостійнр
"""
def my_split(text, delimiter):
    result = []
    start = 0
    for i, char in enumerate(text):
        if char == delimiter:
            result.append(text[start:i])
            start = i + 1
    result.append(text[start:])
    return result

print(my_split("Karamba", "a"))
assert my_split("Karamba", "a") == ['K', 'r', 'mb', '']
