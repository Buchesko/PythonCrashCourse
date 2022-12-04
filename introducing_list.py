# names = ["Kamil", "Marek", "przemek"]
# print(names[2].title())
# print(names[0].upper())
# print(names[1].startswith('M'),names[1].rpartition(' '))
# message = f"My best kolega is {names[1]}"
# print(message.upper())
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# # motorcycles[0] = 'ducati'
# motorcycles.append('ducati')
# print(motorcycles)
# motorcycles = []
# motorcycles.append('ducati')
# motorcycles.append('honda')
# motorcycles.append('hajabuza')
# print(motorcycles)
# del motorcycles[2]
# motorcycles.insert(2, 'yamaha')
# print(motorcycles)
# popped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycles)
# motorcycles = ['honda', 'yamaha', 'suzuki']
# # popping items from list
# last_owned = motorcycles.pop(0)
# print(f"The last motorcycle I owned was a {last_owned.title()}")
# print(motorcycles)
# # Adding item on the last place in the list
# motorcycles.append('ducati')
# print(motorcycles)
# too_expensive = 'ducati'
# # ?removing an item by Value
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive.title()} is too expensive for me")


#Sorting permanently
# cars = ['bmw','audi', 'daihatsu', 'citroen']
# # Sorting permanently
# print(f"Here is the orginal list:\n"+ str(cars))
# # sort list alphabetical order
# cars.sort()
# print(f"Here is the sort list:\n" + str(cars))
# # sort list reversed
# cars.sort(reverse=True)
# print("Here is reversed list:\n" + str(cars))


# Sorting Temporarily
cars = ['bmw','audi', 'daihatsu', 'citroen']
print(f"\nHere is the orginal list:")
print(cars)
print(f"\nHere is the sorted list:")
print(sorted(cars))
print(f"\nHere is the orginal list again:\n" + str(cars) + f"\t\nCompare" + str(sorted(cars))
      + "\nAmount of cars: " + str(len(cars)))
print(cars)



