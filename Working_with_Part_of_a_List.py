# # Slicing a List
# players = ['charles', ' martin', 'michael', 'florence', 'eli']
# print(players[0:5])
# print(players[:4])
# print(players[0:-2])
# print(players[-2:])

# # Looping Through a Slice
# players = ['charles', 'martin', 'michael', 'florence', 'eli']
# print(f"Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())
# # Coping a List
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
#
# print("My favorite foods are: ")
# print(my_foods)
#
# print("\n My friend's favorite foods are:")
# print(friend_foods)
# Defining a Tuple, Krotka
# dimension = (200,50)
# print(dimension[0])
# print(dimension[1])
# Looping through All Values in a Tuple
dimensions = (200,50)
print("Orginal dimension:")
for dimension in dimensions:
    print(dimension)