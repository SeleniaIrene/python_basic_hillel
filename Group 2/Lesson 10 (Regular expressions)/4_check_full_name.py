# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
import re

def check_full_name(full_name: str) -> bool:
    word_pattern = r"^[A-ZА-ЯЄІЇЁҐ][a-zа-яєіїёґьʼ']{1,19}$"
    words = full_name.split()
    if len(words) != 3:
        print(f"Ім'я {full_name} не корректне (має бути 3 частини)")
        return False

    for word in words:
        if not re.match(word_pattern, word):
            print(f"Ім'я {full_name} не корректне (проблема з частиною '{word}')")
            return False

    print(f"Ім'я {full_name} корректне")
    return True

user_name = input("Введіть ваше імʼя: ")
check_full_name(user_name)

assert check_full_name("Оловарь Ірина Андріївна") == True
assert check_full_name("Єва Їжак Йʼордан") == True
assert check_full_name("Anna Maria O'connell") == True
assert check_full_name("Jo Do Sm") == True
assert check_full_name("Abcdefghijklmnopqrst Uvwxyzabcdefghij Klmnopqrstuvwxyzab") == True
assert check_full_name("J Smith") == False
assert check_full_name("John D. Smith") == False
assert check_full_name("Джон Ду") == False
assert check_full_name("John Doe Smith Jr.") == False
assert check_full_name("") == False
