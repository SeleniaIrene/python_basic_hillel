# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
import re

def check_mobile_phone_number(phone_number: str) -> bool:
    pattern = r'^(\+380\d{9}|\d{10})$'
    check = bool(re.match(pattern, phone_number))
    if check == True:
        print(f"Номер {phone_number} корректний")
    else:
        print(f"Номер {phone_number} не корректний")
    return check

user_number = input("Введіть мобільний номер телефону: ")
check_mobile_phone_number(user_number)

assert check_mobile_phone_number("+380955844548") == True
assert check_mobile_phone_number("0955844548") == True
assert check_mobile_phone_number("++380955844548") == False
assert check_mobile_phone_number("") == False
assert check_mobile_phone_number("+38084454") == False
assert check_mobile_phone_number("+3809558445499988") == False
assert check_mobile_phone_number("0955844") == False
assert check_mobile_phone_number("09558445489998") == False
assert check_mobile_phone_number("09558445a8") == False
assert check_mobile_phone_number("+381955844548") == False
assert check_mobile_phone_number("+3800955844548") == False
