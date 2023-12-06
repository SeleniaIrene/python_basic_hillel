# Задача Обміник:
# Намалювати символами табло обміника. Додати 3 валюти. Курс продажу має розраховуватись як на 5% більший ніж покупка.
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

