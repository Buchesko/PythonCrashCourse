# # The while loop in Action
# current_number = 1
# while current_number >5:
#     print(current_number)
#     current_number+=1

# prompt = "\n Tell me something, and i will repeat it back to you: "
# prompt += "\n Enter 'quit' to end the program. "
# message =""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
#

# Using a Flag
# #
# prompt = "\n Tell me something, and i will repeat it back to you: "
# prompt += "\n Enter 'quit' to end the program. "
#
# active = True
# while active:
#
#     newvar = input(prompt)
#     if newvar == 'quit':
#         active = False
#     else:
#         print(newvar)
#
# Using break to exit a loop

# prompt = "\n Please enter the name of a city you have visited : "
# prompt += "\n('Enter 'quit' when you are finished "
#
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"\t I'd love to go to {city.title()}!\n")
# Using continue in a loop
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)
# Praktyka
# prompt = "\nWybierz odpowiednie menu"
# prompt += "\n1. wychodzisz\n2. Kontynuujesz\n3. Przerywasz"
#
#
# active = True
# while active:
#
#     choice = input(prompt)
#     if choice == '1':
#         print("prompt while active = false ")
#         active = False
#     elif choice == '2':
#         print("Prompt continue1")
#         continue
#     elif choice == '3':
#         print("prompt continue2")
#         break
#     else:
#         print("Nie podałeś odpowiedniej wartości")
#         break
