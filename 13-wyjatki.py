countries_and_capitals = {'Poland':'Warsaw',
                          'Czechia':'Prague','Germany':'Berlin'}
# Przechwycenie wyjątku musi być właściwe
try:
    print(2/0)
    print(countries_and_capitals['USA'])
#     warto dodać wyjątek który ma obsługiwać
except KeyError:
    print("Klucz nie został znaleziony")
except ZeroDivisionError:
    print("Nie dziel przez zero")
finally:
    print("zawsze się wykona")
print("Tutaj")

