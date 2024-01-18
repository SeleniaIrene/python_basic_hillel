"""
написати програму яка перетворює список на строку
1) без методів строк
"""
def list_to_string(array):
    result = ''
    for i in array:
        result += str(i)
    return result

a = ["l", "i", "s", "t"]
b = ["l", "i", "s", "t", 5, 1.1]
print(list_to_string(a))
print(list_to_string(b))

assert list_to_string(["l", "i", "s", "t"]) == "list"
assert list_to_string(["l", "i", "s", "t", 5, 1.1]) == "list51.1"

"""
2) з використанням методів строк
"""

def list_to_string2(array):
    result = ''.join((str(i) for i in array))
    return result

a = ["l", "i", "s", "t"]
b = ["l", "i", "s", "t", 5, 1.1]
print(list_to_string2(a))
print(list_to_string2(b))

assert list_to_string2(["l", "i", "s", "t"]) == "list"
assert list_to_string2(["l", "i", "s", "t", 5, 1.1]) == "list51.1"





