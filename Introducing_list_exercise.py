
# names_list = [f"Adam", "Marek", "Zbigniew"]
# tables = 1
# guest_per_table = 2
# max_cap = tables * guest_per_table
# guest_amount = len(names_list)
# if guest_amount > max_cap:
#     print(f"{guest_amount} exceeds {max_cap}")
# elif guest_amount < max_cap:
#     print(f"W restauracji są {tables} stoliki więc moge zaprosić tylko {guest_per_table * tables} gości\n")
# print(names_list)
# # print(guest_amount * tables)
# # names = input("")

# names_list_guest = [f"mariusz", "przemek", "viktor"]
#
# print(names_list_guest[0].title() + f" I invite you to diner" + "\n"
#       + names_list_guest[1].title() + f" I invite you to diner" + "\n"
#       + names_list_guest[2].title() + f" I invite you to diner")
# print(names_list_guest)
#
# print(f"I get massage from " + names_list_guest.pop(2).title() + f" not came to diner")
# names_list_guest.append("andrzej")
# print(names_list_guest[0].title() + f" I invite you to diner" + "\n"
#       + names_list_guest[1].title() + f" I invite you to diner" + "\n"
#       + names_list_guest[2].title() + f" I invite you to diner")
# print(names_list_guest)
# names_list_guest.insert(0, "monika")
# names_list_guest.insert(2, "jesica")
# names_list_guest.append("veronika")
# print(names_list_guest)
# guest_amount = len(names_list_guest)
# print(guest_amount)
#
# print(names_list_guest[0].title() + f" I invite you to diner" + "\n"
#       + names_list_guest[1].title() + f" I invite you to diner" + "\n"
#       + names_list_guest[2].title() + f" I invite you to diner" + "\n"
#       + names_list_guest[3].title() + f" I invite you to diner" + "\n"
#       + names_list_guest[4].title() + f" I invite you to diner" + "\n"
#       + names_list_guest[5].title() + f" I invite you to diner" )
# Pentla wyswietlajaca listę gości
names_guest_list = ['andrzej', 'bartosz', 'czarek']
for name in names_guest_list:
    print(f"{name.title()}, I invite you to diner")

# names = names_list_guest.pop(5)
# print(f"Sorry " + names.title() + " there's no room at the table.")
# names = names_list_guest.pop(4)
# print(f"Sorry " + names.title() + " there's no room at the table.")
# names = names_list_guest.pop(3)
# print(f"Sorry " + names.title() + " there's no room at the table.")
# names = names_list_guest.pop(2)
# print(f"Sorry " + names.title() + " there's no room at the table.")
# confirm_guest_amount = len(names_list_guest)
# print(confirm_guest_amount)
# print(names_list_guest[0].title() + f" I invite you to diner" + "\n"
#       + names_list_guest[1].title() + f" I invite you to diner" + "\n")
# while len(names_list_guest) == 2:
#     names_list_guest.pop()
#     names_list_guest.pop()
#     print(names_list_guest)
# del(names_list_guest[1])
# del(names_list_guest[0])
# print(names_list_guest)
# while guest_amount == 2:
#     for names in names_list_guest:
#         print((names.title()) + f" I invite you to diner")
# def places(place_for_travel, names_list) :
#     place_for_travel = ['paris', 'warszawa', 'barcelona', 'den haag', 'gdańsk']
#     names_list = ['Martin', 'Mohamed', 'mirko', 'leokadia', 'Nani', 'Nicola', 'Kadir']
#     return place_for_travel, names_list
# print(places(place_for_travel=True, names_list=True))
# place_for_travel lista sortowana tymczasowo
place_for_travel = ['paris', 'warszawa', 'barcelona', 'den haag', 'gdańsk']
print(f"This is list place for travel\t" + str(place_for_travel).title())
print(f"Sorted Alphabetical\t" + str(sorted(place_for_travel)).title() + f"\tOrginal list "+str(place_for_travel))
print(f"This is list place for living again\t" + str(place_for_travel).title())
print(f"This is list printed reversal: " + str(sorted(place_for_travel, reverse=True )).title()
      + "tOrginal list" + str(place_for_travel))

# Permanentne sortowanie
place_for_travel.sort()
print(f"Permanent sort\n"
      + f"Sorted Alphabetical\t" + str(place_for_travel).title()
      + "tOrginal list" + str(place_for_travel).title())
place_for_travel.sort(reverse=True)
print(f"Permanent sort\n"
      + f"Sorted Reversed\t" + str(place_for_travel).title()
      + "\tOrginal list" + str(place_for_travel).title())
# Odwrócone sortowanie
place_for_travel.reverse()
print(place_for_travel)
place_for_travel.reverse()
print(place_for_travel)
