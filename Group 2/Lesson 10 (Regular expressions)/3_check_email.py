# - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
import re

def check_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9]{2,}([a-zA-Z0-9._-]{1,})?[a-zA-Z0-9]{1,}\@[a-zA-Z0-9.-]{2,}\.[a-zA-Z]{2,}$'
    check = bool(re.match(pattern, email))
    if check == True:
        print(f"Адреса {email} корректна")
    else:
        print(f"Адреса {email} не корректна")
    return check

user_email = input("Введіть ваш email: ")
check_email(user_email)

assert check_email("selenia.irish@gmail.com") == True
assert check_email("seleni@bk.ru") == True
assert check_email("Iryna.Olovar@fintech-farm.com") == True
assert check_email("s"*50 + "@ukr.net") == True
assert check_email("selenia_irisha@ukr.net") == True
assert check_email("_selenia@ukr.net") == False
assert check_email("selenia.@ukr.net") == False
assert check_email("selenia@a.a") == False
assert check_email("selenia@ttt") == False
assert check_email("s@t.co") == False
assert check_email("") == False