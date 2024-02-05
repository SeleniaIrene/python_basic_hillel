# 1. Даний текстовий файл. Необхідно створити новий файл,
# який потрібно переписати з першого файлу всі слова,
# що складаються не менше ніж з семи літер.
import re

with open("home_work.txt", "r") as myfile:
     lines = []
     while True:
         one_line = myfile.readline()
         if not one_line:
             break
         lines.append(one_line.strip())

     origin_line = ' '.join(lines)
     words = origin_line.split()

     pattern = r"^[A-ZА-ЯЄІЇЁҐa-zа-яєіїёґьʼ']{7,}$"
     long_words = []
     for word in words:
         if re.match(pattern, word):
             long_words.append(word)

     print(long_words)

     with open("output_find_words_more_7_char.txt", "w") as file:
         file.write(" ".join(long_words))
