# - домашній номер телефону (тільки цифри та довжина номера)
import re

def check_home_phone_number(phone_number: str) -> bool:
    pattern = r'^\d{6}$'
    check = bool(re.match(pattern, phone_number))
    if check == True:
        print(f"Номер {phone_number} корректний")
    else:
        print(f"Номер {phone_number} не корректний")
    return check

user_number = input("Введіть домашній номер телефону: ")
check_home_phone_number(user_number)

assert check_home_phone_number("123456") == True
assert check_home_phone_number("654321") == True
assert check_home_phone_number("1") == False
assert check_home_phone_number("123456789") == False
assert check_home_phone_number("123abc") == False
assert check_home_phone_number("abcdef") == False
assert check_home_phone_number("123 456") == False
assert check_home_phone_number("123-456") == False
assert check_home_phone_number("") == False
