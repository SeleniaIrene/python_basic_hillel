# 3. Створіть програму, яка перевіряє текст на неприпустимі слова.
# Якщо неприпустиме слово знайдено, його слід замінити на набір символів *.
# За підсумками роботи програми необхідно показати статистику дій.

def replace_unacceptable_word(correction_file: str, unacceptable_words: list) -> int:
    with open(correction_file, "r") as file:
        content = file.read()
        words = content.split()
        actions_cnt = 0
        new_words = []

        for word in words:
            cleaned_word = word.strip('.,;:!?\'"')
            if cleaned_word.lower() in [unacceptable_word.lower() for unacceptable_word in unacceptable_words]:
                replacement = '*' * len(cleaned_word)
                new_word = word.replace(cleaned_word, replacement)
                new_words.append(new_word)
                actions_cnt += 1
            else:
                new_words.append(word)

    modified_text = ' '.join(new_words)
    print("Замінено неприпустимі слова:", actions_cnt)
    print(f"Модифікований текст: \n{modified_text}")

    return actions_cnt

#Виконання функції
correction_file_1 = "home_work.txt"
unacceptable_words_1 = ["літо", "123456789", "@#$%test", "!@_&tes", "test"]
replace_unacceptable_word(correction_file_1, unacceptable_words_1)

print()

#Виконання функції (тест №2)
with open("test_file.txt", "w") as test:
    test.write("To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep; No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation Devoutly to be wish'd. To die, to sleep")

correction_file_2 = "test_file.txt"
unacceptable_words_2 = ["die"]
replace_unacceptable_word(correction_file_2, unacceptable_words_2)


