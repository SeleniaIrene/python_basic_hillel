"написати фунцію переводу з римськох системи числення до десятичної"

roman_numerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

import re
def from_roman(rom):
    dec = 0
    prev_value = 0
    start_rom = rom
    regex_pattern = re.compile('|'.join(f'{key}{{4,}}' for key in roman_numerals.keys()))

    try:
        if any(char not in roman_numerals for char in rom):
            raise ValueError("Введені символи не відповідають літерам римської системи")
        elif regex_pattern.search(rom):
            raise ValueError("Символи не повинні повторюватися більше трьох разів")
    except ValueError as e:
        print(e)
        return str(e)

    else:
        for char in rom:
            value = roman_numerals[char]
            if prev_value < value:
                dec += value - 2 * prev_value
            else:
                dec += value
            prev_value = value

    print(f"{start_rom} = {dec}")
    return dec

#user_number = input("Введіть число у римській системі числення: ").upper()
#from_roman(user_number)

assert from_roman("I") == 1
assert from_roman("IV") == 4
assert from_roman("IX") == 9
assert from_roman("LVIII") == 58
assert from_roman("XCIV") == 94
assert from_roman("C") == 100
assert from_roman("CDXLIV") == 444
assert from_roman("CM") == 900
assert from_roman("MCMXCIV") == 1994
assert from_roman("kkkddd") == "Введені символи не відповідають літерам римської системи"
assert from_roman("IIII") == "Символи не повинні повторюватися більше трьох разів"

