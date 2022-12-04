# cars =['audi', 'bmw', 'subaru','toyota']
# for car in cars:
#     if car =='bmw':
#         print(car.upper())
#     else:
#         print(car.title())
# # Testing condition 1
# car = 'subaru'
# print("Is car == 'subaru'? I predict, True")
# print(car == 'SuBarU'.lower())
# print("Is car is 'audi' ? I predict false")
# print(car == 'audi')
# # Testing condition 2
# lista1 = ['ania','magda']
# lista2 = ['ania','grażyna']
# if lista1 == lista2:
#     print("Takie same")
# else:
#     print("Difrences")
# # Testing condition 3
# list3 = ['basia', 'marysia']
# if 'marysia' in list3:
#     print("True")
# else:
#     print("False")
# # Test conditions 4
# names = lista1 + lista2 + list3
# amount = len(names)
# print(amount)
# if len(names) <=7 and amount == 6:
#     print("complet")
# print(names)
# # test condition 5
# age_1 = 22
# age_2 = 18
# print()


# # Checking for Inequality
# request_topping = 'mushrooms'
#
# if request_topping != "Anchovies":
#     print("Hold the anchovies")
# #     Numerical comparition
# age = 18
# if age == 18:
#     print()

# cars =['audi', 'fiat', 'kurde']
# # cars = str(cars).upper()
# var1 = str(cars).islower()
# if var1 == True:
#     print("Prawda !!")
# else:
#     print("Fałsz!!")
## The if-elif-else chain
# alien_color = 'red'
# if alien_color == 'green':
#     score = 5
#     print("Your score is 5")
# else:
#     score = 0
#     print(f"Your score is 0 and alien color is {alien_color}")
# #
# users = ['admin','login', 'user']
# for users in users:
#     if users == 'admin':
#         print(f"Greetengs {users.title()}. Lets make new rules")
#     else:
#         print(f"Greetings {users.capitalize()}, Thank you for login again")
emotion_scale = input("Type how you feel in range 1-100")
if str(emotion_scale).isdigit() == True:
    if emotion_scale == 0:
        print("Nie czujesz nic")
    elif emotion_scale < 25:
        print("Arousal reduction")
    elif emotion_scale > 25 and emotion_scale > 50:
        print("Light arousal")
    elif emotion_scale > 50 or emotion_scale < 75:
        print("midle Arousal")
    elif emotion_scale > 75:
        print("Arousal emotion")
else:
    print("Watch out wht you are typing")


