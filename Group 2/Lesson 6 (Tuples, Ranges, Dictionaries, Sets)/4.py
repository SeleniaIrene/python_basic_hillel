# Словники:
# 1. Наведено список країн і міст кожної країни. Для кожного міста вкажіть, в якій країні воно знаходиться.
# Приклад результату:
# {"Ukraine": ["Kyiv", "Lviv", "Dnipro"],"USA": ["Los Angeles", "Las Vegas"]}

# Ініціалізація порожнього словника
countries_cities_dict = {}

while True:
    country = input("Введіть назву країни (або 'стоп' для завершення): ")
    if country == 'Стоп':
        break
    cities = []
    while True:
        city = input(f"Введіть назву міста у {country} (або 'стоп' для завершення): ")
        if city == 'Стоп':
            break
        cities.append(city)
    countries_cities_dict[country] = cities

print(countries_cities_dict)
