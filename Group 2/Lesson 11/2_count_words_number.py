#2. Даний текстовий файл. Підрахувати кількість слів у ньому.
import re

with open("home_work.txt", "r") as file:
    content = file.read()
    words = content.split()
    pattern = r"^[A-ZА-ЯЄІЇЁҐa-zа-яєіїёґьʼ']+$"

    num_words_and_numbers = len(words)
    num_words = len([word for word in words if re.match(pattern, word)])

    print(f"Кількість слів (в тому числі цифр і символів) в тексті: {num_words_and_numbers}")
    print(f"Кількість слів в тексті: {num_words}")
