# - Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра, один символ, довжина пароля – від 8 до 16 символів)
import re

def check_password(password: str) -> bool:

    if (len(password) < 8 or len(password) > 16):
        print(f"Пароль {password} не є корректним (невідповідна довжина)")
        return False

    if re.search(r'\s', password):
        print(f"Пароль {password} не є корректним (містить пробіли)")
        return False

    has_lower, has_upper, has_digit, has_symbol = False, False, False, False
    for char in password:
        if re.match(r'[a-z]', char):
            has_lower = True
        elif re.match(r'[A-Z]', char):
            has_upper = True
        elif re.match(r'[0-9]', char):
            has_digit = True
        elif re.match(r'[!*@#$%^&+=]', char):
            has_symbol = True
    if not (has_lower and has_upper and has_digit and has_symbol):
        print(f"Пароль {password} не є корректним")
        return False

    print(f"Пароль {password} є корректним")
    return True

user_password = input("Введіть ваш пароль: ")
check_password(user_password)

assert check_password("Admin123!") == True
assert check_password("Qw@rty$7") == True
assert check_password("Bb2@bbbbbbbbbbbb") == True
assert check_password("Aa1!") == False
assert check_password("admin123!") == False
assert check_password("aaaa@aa1") == False
assert check_password("Pass1234?") == False
assert check_password("Admin &123") == False

