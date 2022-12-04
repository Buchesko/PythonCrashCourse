# # Simply dicrionary
# alien_0 = {'color': 'green', 'points':5}
# new_points = alien_0['points']
# alien_0['x_position'] = 0
# alien_0['y_points'] = 25
# print(alien_0['color'])
# print(alien_0['points'])
# print(f"You just earned {new_points} points")
# print(alien_0)
# # Starting with empty list
# alien_0 = {}
# alien_0['color'] ='green'
# alien_0['points'] = 5
# print(alien_0)
# # Modifying Values in a Dictionary
# alien_0 = {'color':'green'}
# print(f"The alien color is {alien_0['color'].title()}")
# alien_0['color'] = 'yellow'
# print(f"The alien color is {alien_0['color'].title()}")
# # Example
# alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
# print(f"Orginal position {alien_0['x_position'],alien_0['y_position']}")
# # Move the alien to the right
# # Determine how far to move the alien based on its current speed
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     #     it has to be fast alien
#     x_increment = 3
# # the new position is the old position plus increment
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position {alien_0['x_position'], alien_0['y_position']}")
# # Removing key-Value pairs
# alien_0 = {'color':'green', 'points':5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)

# # Dictionary similar object
# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c#',
#     'edward':'ruby',
#     'phil': 'python'
# }
# language = favorite_language['sarah'].title()
# print(f"Sarah favorite language is {language}")

# Using get() to Acces Values
# alien_0 = {'color':'green', 'speed':'slow','points':0}
# # print(alien_0['points'])
# point_value = alien_0.get('points','No points value assigned')
# print(point_value)

# Looping through a dictionary
# user_0 = {
#     'username':'buchesko',
#     'first_name':'Lukasz',
#     'last_name':'Kuchta',
# }
# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")
# Administrator chatu
# administrator forum

# Nesting
# #  A list of dictionaries
# alien_0 = {'color':'green', 'points': 5}
# alien_1 = {'color':'yellow', 'points': 10}
# alien_2 = {'color':'red', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#     print(alien)
#
# # Make a empty list for storing aliens
# aliens = []
#
# # make 30 green aliens
#
# for alien_number in range(30):
#     new_alien = {'color':'yellow', 'points': 5, 'speed':'slow'}
#     aliens.append(new_alien)
#
# # Modyfiction 3 aliens
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] ='yellow'
#         alien['speed'] ='medium'
#         alien['points'] = 10
#     elif alien['color'] =='yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15
#
#
#
# # Show the firs 5 alien
#
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# # Show how many aliens have been created
# print(f"Total number of aliens: {len(aliens)}")

# List in a dictionaries
# Storing information about a pizza being order.
#
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }
# # Summarize the order.
# print(f"You order a {pizza['crust']} - crust pizza" +"\n"+
#       "with following toppings:")
# for topping in pizza['toppings']:
#     print(f"\t{topping}")
#
# # Jedno ćwiczenie na partie a wiele cwiczeń na partie
# workout = {
#     'klata': 'bench press',
#     'core':['sit ups', 'superman',],
# }



# # #  Praktyka
# # week_number = ()
# workout_name = input('Podaj nazwę cwiczenia')
# workout_weight = int(input('Podaj obciążenie'))
# workout_sets = input('Podaj ilość setów')
# workout_reps = input('Podaj ilość powtórzeń')
# workouts = {
#     'chess_workout': {
#         'name_workout':workout_name,
#         'weight':workout_weight,
#         'sets':workout_sets,
#         'reps':workout_reps,
#     },
# }
# for workout,workout_info in workouts.items():
#     performance = f"{workout_info['weight']} KG, {workout_info['sets']} Sets, {workout_info['reps']} reps"
#     print(f" Cwiczenie : {workout_name}")
#     print(f"Osiągi: {performance}")
# print(workouts)
# print(f" week {['']}")
# for week_number in range (1,52):
#     if week_number == 24:
#         week_number_increment = 1
#         workout_weight_increment = 5
#
#
# # workout[week_number] = workout[week_number] + week_number_increment
# workout['weight'] = workout['weight'] + workout_weight_increment
# print(f"Podgląd {workout['weight']}")




