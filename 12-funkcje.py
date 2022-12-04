countries_information = {}
countries_information["Polska"] = ("Warszawa", 37.97)
countries_information["Niemcy"] = ("Berlin", 83.02)
countries_information["Słowacja"] = ("Bratysława", 5.45)

def show_country_info(country):
    country_information = countries_information.get(country)
    print("\n")
    print(country)
    print(f"Stolica: " + country_information[0] + "\n"
        + f"Liczba mieszkańców mln: " + str(country_information[1]))
for country in countries_information.keys():
    print(country)
country = input("Informacje o jakim kraju chcesz wyświetlić")
show_country_info(country)

# def display_sum(a, b):
#     print(a + b)
#     return a + b
# sum = display_sum(3,5)
# print(display_sum(2,5) + sum + sum)
# Przypisujemy argument zmiennej jesli coś zwraca
# def calculate_sum(a,b):
#     return a + b
# sum = calculate_sum(2,5)
# print(sum)

def print_message():
    print("To jest wiadomość")



