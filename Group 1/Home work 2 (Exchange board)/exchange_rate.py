# Задача Обміник:
# Намалювати символами табло обміника. Додати 3 валюти.
# Курс продажу має розраховуватись як на 5% більший ніж покупка.
# Також відформувати вивод обмінику. Щоб сумми отриманих грошей і решти були на одному рівні.
# Шаблон табло
# **************
# *BUY   SELL  *
# *100 EUR 105 *
# *40 USD 43   *
# *2  PLN 3    *
# **************

UAH_USD = 36.71
UAH_EUR = 39.54
UAH_PLN = 9.14
UAH_DKK = 5.3
UAH_GBP = 46.12

amount_uah = int(input("Enter amount of UAH: "))
buy_uah_usd = amount_uah // UAH_USD
sell_uah_usd = amount_uah // (UAH_USD * 0.95)
buy_uah_eur = amount_uah // UAH_EUR
sell_uah_eur = amount_uah // (UAH_EUR * 0.95)
buy_uah_pln = amount_uah // UAH_PLN
sell_uah_pln = amount_uah // (UAH_PLN * 0.95)
buy_uah_dkk = amount_uah // UAH_DKK
sell_uah_dkk = amount_uah // (UAH_DKK * 0.95)
buy_uah_gbp = amount_uah // UAH_GBP
sell_uah_gbp = amount_uah // (UAH_GBP * 0.95)

print("*"*31)
print("* BUY", " "*18, "SELL *")
print(f"* {buy_uah_usd:<11} USD {sell_uah_usd:>11} *")
print(f"* {buy_uah_eur:<11} EUR {sell_uah_eur:>11} *")
print(f"* {buy_uah_pln:<11} PLN {sell_uah_pln:>11} *")
print(f"* {buy_uah_dkk:<11} DKK {sell_uah_dkk:>11} *")
print(f"* {buy_uah_gbp:<11} GBP {sell_uah_gbp:>11} *")
print("*"*31)

# Розширити функціонал обмінника. Додати можливість обирати операцію(купівля продаж).
# Для простоти лише в парі долар-гривня 50 балів
# При купівлі долару, якщо сумма в долларах близька до суми кратній 50 запропонувати взяти рівну суму.
# Або повернути зайві гривні або попросити доплатити.
# Та розрахувати нову сдачу в гривні, з урахуванням нової суми. Критерій близкості 5%.
# Зауважте, що в майбутньому критерій близкості та кратність може змітинись.
# Ці параметри мають зберігатись в константах, щоб ми мали змогу швидко їх змінити при необхідності.

operation = input("Choose an operation (purchase - 'buy', sale - 'sell'): ").lower()

if operation == 'buy':
    print(f"{buy_uah_usd} USD")
elif operation == 'sell':
    print(f"{sell_uah_usd} USD")
else:
    print("You have entered an incorrect operation. Enter buy or sell")

# Константи для критеріїв близькості та кратності
CLOSENESS_THRESHOLD = 0.05
MULTIPLE = 50
change_uah = amount_uah % (buy_uah_usd * UAH_USD)

if operation == 'buy':
    print(f"Вы получите {buy_uah_usd} USD, сдача {change_uah:.0f} UAH.")

    if buy_uah_usd % MULTIPLE != 0:
        nearest_multiple = round(buy_uah_usd / MULTIPLE) * MULTIPLE
        difference = nearest_multiple - buy_uah_usd

        closeness = abs(difference / nearest_multiple)
        if closeness <= CLOSENESS_THRESHOLD:
            extra_to_pay = difference * UAH_USD
            print(f"Чтобы купить {nearest_multiple}$, внесите {extra_to_pay:.2f} гривен.")
            decision = input("Хотите внести недостающую сумму? (Y/n): ").lower()

            if decision == 'y':
                extra_payment = float(input("Введите сумму доплаты в гривнах: "))
                amount_uah += extra_payment
                new_buy_uah_usd = amount_uah // UAH_USD

                if new_buy_uah_usd % MULTIPLE == 0:
                    print(f"Вы получите {new_buy_uah_usd} USD, сдача {amount_uah % (new_buy_uah_usd * UAH_USD):.0f} UAH.")
                else:
                    new_change_uah = amount_uah % (new_buy_uah_usd * UAH_USD)
                    print(f"Вы получите {new_buy_uah_usd} USD, сдача {new_change_uah:.0f} UAH.")
            else:
                print(f"Вы получите {buy_uah_usd} USD, сдача {change_uah:.0f} UAH.")
        else:
            extra_to_pay = difference * UAH_USD
            print(f"Вам необходимо внести дополнительные гривны, чтобы купить {nearest_multiple}$. Внесите {extra_to_pay:.2f} гривен.")

