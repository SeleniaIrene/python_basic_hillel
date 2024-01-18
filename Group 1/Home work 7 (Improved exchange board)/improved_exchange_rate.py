#Облаштувати Переведення валют в обмінику через словник(приклад структури на гітхабі)
#Загорнути код що робить конвертацію та розраховує курс продажу в фунції.
#В словнику дані кількість купюр кожного номіналу. Зробити фунцію яка перевіряє чи вистачить коштів чи купюр щоб обміняти гроші..

PROFIT_PRC = 0.05

current= {
    "UAH": {
        "buy": {
            "USD": 37
           ,"EUR": 40
           ,"PLN": 9
           ,"DKK": 5
           ,"GBP": 46
        }
       ,"sell": {}  # Порожній словник для запису даних про продаж
    }
}

# Для кожної валюти вираховуємо вартість продажу
for currency, buy_price in current["UAH"]["buy"].items():
    sell_price = buy_price * (1 + PROFIT_PRC)  # Вартість продажу = вартість покупки + прибуток
    current["UAH"]["sell"][currency] = int(round(sell_price,0))

amount = int(input("Введіть суму, яку хочете обміняти: "))
operation = input("Виберіть операцію (купівля - buy, продаж - sell): ")
to_currency = input("Введіть назву валюти (USD, EUR, PLN, DKK, GBP): ")

def convert_currency(amount, operation, to_currency):
    if operation == "buy":
        rate = current['UAH']["buy"][to_currency]
        result = amount // rate
        remain = amount % rate
        print(f"Ви отримаєте {result} {to_currency}")
        print(f"Ваша решта {remain} грн")
    elif operation == "sell":
        rate = current['UAH']["sell"][to_currency]
        result = amount * rate
        remain = 0
        print(f"Ви отримаєте {result} {'UAH'}")
    else:
        print("Ви ввели неправильну операцію. Введіть buy або sell")
    return result

new_currency_amount = convert_currency(amount, operation, to_currency)

availability_banknotes = {100:2, 50:10, 20:0, 10:0, 5:100, 2:10, 1:10}

def check_exchange(remaining_amount, currency, availability):
    if operation == "buy":
        denominations = sorted(availability.keys(), reverse=True)
        print(f"Можливий обмін {remaining_amount} {currency} на купюри:")
        for note in denominations:
            if note <= remaining_amount and availability[note] > 0:
                num_notes = min(availability[note], remaining_amount // note)
                remaining_amount -= num_notes * note
                availability[note] -= num_notes
                print(f"{num_notes} купюр по {note} {currency}")

check_exchange(new_currency_amount, to_currency, availability_banknotes)
