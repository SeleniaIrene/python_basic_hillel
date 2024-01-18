"""
№1Доробити задачку на дужки з урахуванням того, що в нас можуть бути 3 типи дужок,
а між дужками довільна кількість символів
"""

brackets = {")": "(", "}": "{", "]": "["}

def check_parenthes(string):
    stack = []
    for char in string:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or brackets[char] != stack.pop():
                return False
    if len(stack) > 0:
        return False
    return True  # Перевірка на збалансованість

assert check_parenthes("()()") == True
assert check_parenthes("(())") == True
assert check_parenthes(")(") == False
assert check_parenthes("()(") == False
assert check_parenthes(")())") == False
assert check_parenthes("({})") == True
assert check_parenthes("(})") == False
assert check_parenthes("{{{}}}()") == True
assert check_parenthes("[({})]") == True
assert check_parenthes("({})]") == False
assert check_parenthes("[({aaaaaa})]") == True
assert check_parenthes("[&&^*#&^({nkbu}   )]") == True

"""
#Менш оптимальний варіант
def check_parenthes(string):
    stack1 = []
    stack2 = []
    stack3 = []
    for char in string:
        if char == "(":
            stack1.append(char)
        elif char == ")" and stack1 and stack1[-1] == "(":
            stack1.pop()
        elif char == "{":
            stack2.append(char)
        elif char == "}" and stack2 and stack2[-1] == "{":
            stack2.pop()
        elif char == "[":
            stack3.append(char)
        elif char == "]" and stack3 and stack3[-1] == "[":
            stack3.pop()
        else:
            return False  # Неспівпадіння дужок
    if len(stack1) > 0 or len(stack2) > 0 or len(stack3) > 0:
        return False
    return True  # Перевірка на збалансованість
    """