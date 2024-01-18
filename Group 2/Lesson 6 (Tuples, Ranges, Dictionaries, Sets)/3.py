# 3. Даний текст: у першому рядку записано число рядків, далі йдуть самі рядки.

verse = [
4
,'І все на світі треба пережити,'
,'І кожен фініш – це, по суті, старт,'
,'І наперед не треба ворожити,'
,'І за минулим плакати не варт.'
]

verse_as_string = [str(item) for item in verse]
verse_as_text = ' '.join(verse_as_string)

# Вилучити число з тексту
found_number = ''
for char in verse_as_text:
    if char.isdigit():
        found_number += char

verse_as_text_without_number = verse_as_text.replace(found_number, '')

# Визначте, скільки унiкальних слів міститься у цьому тексті.
# Словом вважається послідовність непробільних символів, що йдуть поспіль,
# слова розділені одним або більшим числом пробілів або символами кінця рядка.

words = []
current_word = ''

for char in verse_as_text_without_number:
    if char in ['.', ',', '–', ' ']:
        if current_word:
            words.append(current_word)
            current_word = ''
    else:
        current_word += char

unique_words = set(words)
print("Кількість унікальних слів:", len(unique_words))
print("Унікальні слова:", unique_words)