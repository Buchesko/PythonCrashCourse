
# List
# names_list = []
# names_list.append("Kamil")
# names_list.append("Mariusz")
names_list = [f"Kamil", "Mariusz", "Adam", "Kamil"]
# names_list.reverse()
# print(names_list)
# names_list.sort()
print(names_list[0])
# print(names_list)
# print(names_list.pop(0))
# print(names_list)
# for name in names_list:
# print(name)
# print(names_list.count("Kamil"))
# print(len(names_list))
# names_list = ["kamil", "marek", "marek", "jarosław"]
# name_list1 = ["junior"]
# name_list2 = ["grzesiek"]
# name_list3 = names_list + name_list1 + name_list2
# names_list.sort()
# names_list.sort(reverse=True)
# print(names_list)

# krotka brak mozliwosci jakich kolwiek zmian
# names_list = ("kamil", "marek", "marek", "jarosław")
# person = ("Lukasz", "Kuchta", 34)
# print(len(person))
# print(person.count("Lukasz"))
# print(person)

# Set
# dictionary
#  cechy setu nie mogą powtarzac się wartości, elementy setu nie mutowalne, nie są uporządkowane
# names_set = set()
# names_set.add("Kamil")
# names_set.add("Dominik")
# names_list = []
# names_tuple = ("Andrzej")

# dodajac liste do setu nie zadziala
# names_set.add(names_list)

# dodajac krotke set zadziała
# names_set.add(names_tuple)
# names_set.remove("Andrzej")

# różnica między dwoma metodami, jeśli dodamy met remove z nie istniejącym kluczem to program zwróci wartość KeyError: 'Andrzej'
# names_set.discard("Andrzej")
# names_set = {"Kamil", "Mariusz"}
# print(names_set)
# for names in names_set:
#     print(names)

names_set = set()
names_set.add("Kamil")
names_set.add("Dominik")
names_set1 = {"andrzej", "lukasz", "Kamil"}
names_set2 = names_set.union(names_set1)
names_set.update(names_set1)
print(names_set)

# roznice miedzy dwoma setami
# names_set2 = names_set.difference(names_set1)
# czesc wspolna
# names_set2 = names_set.intersection(names_set1)
# wszystkie roznice z wyjatkiem czesci wspolnych

# names_set2 = names_set.symmetric_difference(names_set1)
# names_set1.clear()
# names_list = ["Rafał", "Zbigniew"]


# names_list.extend(names_set1)
# for names in names_set1:
#     print(names.title())

# Dictionary
# coutries_and_capitals = {"Poland":"Warsaw","German":"Berlin" }
# coutries_and_capitals['Czehia'] = "Prague"
# print(coutries_and_capitals)

# sprawdzamy klucze
# for country in coutries_and_capitals.keys():
# print(country)

# sprawdzamy wartości
# for capitol in coutries_and_capitals.values():
#     print(capitol.title())
# for country, capital in coutries_and_capitals.items():
#     print(country + "-" + capitol)

# print(coutries_and_capitals["USA"])
# KeyError: 'USA'
# print(coutries_and_capitals.get("USA", "Washinton DC"))
# Washington
# print(coutries_and_capitals.get("USA")
# none
# print(coutries_and_capitals.setdefault("USA", "Washington"))
# Washington
# {'Poland': 'Warsaw', 'German': 'Berlin', 'Czehia': 'Prague', 'USA': 'Washington'}
# print(coutries_and_capitals.setdefault("Poland", "Washington"))
# Warsaw
# {'Poland': 'Warsaw', 'German': 'Berlin', 'Czehia': 'Prague'}
# print(coutries_and_capitals)

# coutries_and_capitals["Poland"] ="Cracow"
# print(coutries_and_capitals)
# {'Poland': 'Cracow', 'German': 'Berlin', 'Czehia': 'Prague'}

# coutries_and_capitals.pop("USA")
# KeyError: 'USA'

# print(coutries_and_capitals.pop("USA", "Washington DC"))
# print(coutries_and_capitals)
# Washington DC
# {'Poland': 'Warsaw', 'German': 'Berlin', 'Czehia': 'Prague'}

# print(coutries_and_capitals.popitem())
# print(coutries_and_capitals)
# ('Czehia', 'Prague')
# {'Poland': 'Warsaw', 'German': 'Berlin'}

# print( "Poland" in coutries_and_capitals)
# True
# print("USA" in coutries_and_capitals)
# False

# if "Poland" in coutries_and_capitals.keys():
#     print("Znaleziono!")
# else:
#     print("Nie znaleziono!")


