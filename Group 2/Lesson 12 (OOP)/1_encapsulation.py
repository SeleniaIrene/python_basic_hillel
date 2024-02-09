# Завдання 1:
# Створіть клас "Місто". Необхідно зберігати в полях класу:
# назву міста, назву регіону, назву країни, кількість жителів міста,
# поштовий індекс міста, телефонний код міста.
# Реалізуйте доступ до окремих полів (Інкапсуляція).

class City:
    __city_name = "no name"
    __region = "no name"
    __country = "no name"

    def __init__(self, city_name, region, country, num_inhabitants, postal_code, phone_code):
        self.city_name = city_name
        self.region = region
        self.country = country
        self.num_inhabitants = num_inhabitants
        self.postal_code = postal_code
        self.phone_code = phone_code

    @property  # getter -> для того чтобы получить доступ к приватному полю
    def city_name(self):
        return self.__city_name

    @city_name.setter  # setter -> для того чтобы получить доступ к приватному полю и изменить его значение
    def city_name(self, city_name):
        if isinstance(city_name, str) and len(city_name) > 1:
            self.__city_name = city_name
        else:
            print("Incorrect city")

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if isinstance(region, str) and len(region) > 1:
            self.__region = region
        else:
            print("Incorrect region")

    @property
    def country(self):
        return self.__region

    @country.setter
    def country(self, country):
        if isinstance(country, str) and len(country) > 1:
            self.__country = country
        else:
            print("Incorrect country")

    def show_info(self):
        print(f"City: {self.city_name}, "
              f"region: {self.region}, "
              f"country: {self.country}, "
              f"number of inhabitants: {self.num_inhabitants}, "
              f"postal code: {self.postal_code}, "
              f"phone code: {self.phone_code}")

Dnipro = City("Dnipro", "Dnipro", "Ukraine", 1000000, 49130, "056")
Dnipro.show_info()
Test_city = City("a", 11, "", 65000, 130, "076")
Test_city.show_info()


# Завдання 2:
# Створіть клас "Країна". Необхідно зберігати в полях класу: назву країни,
# назву континенту, кількість жителів країни, телефонний код країни, назву столиці,
# назву міст країни. Реалізуйте доступ до окремих полів (Інкапсуляція).

class Country:
    __country_name = "no name"
    __continent = "no name"

    def __init__(self, country_name, continent, num_inhabitants, phone_code, capital, cities_name):
        self.country_name = country_name
        self.continent = continent
        self.num_inhabitants = num_inhabitants
        self.phone_code = phone_code
        self.capital = capital
        self.cities_name = cities_name

    @property
    def country_name(self):
        return self.__country_name

    @country_name.setter
    def country_name(self, country_name):
        if isinstance(country_name, str) and len(country_name) > 1:
            self.__country_name = country_name
        else:
            print("Incorrect country")

    @property
    def continent(self):
        return self.__continent

    @continent.setter
    def continent(self, continent):
        if isinstance(continent, str) and len(continent) > 1:
            self.__continent = continent
        else:
            print("Incorrect continent")

    def show_info(self):
        print(f"Country: {self.country_name}, "
              f"continent: {self.continent}, "
              f"number of inhabitants: {self.num_inhabitants}, "
              f"phone code: {self.phone_code}, "
              f"capital: {self.capital}, "
              f"cities: {self.cities_name}")

Ukraine = Country("Ukraine", "Europe", 65000000, "+380", "Kyiv", "Dnipro")
Ukraine.show_info()
Test_country = Country("", 111, 1000000, "+090", "Aaaa", "Aaaa, Bbbb")
Test_country.show_info()
