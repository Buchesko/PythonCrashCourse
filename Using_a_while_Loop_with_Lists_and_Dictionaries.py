# Moving Items ftom One List to another
# Start with users that need to be verfied
#  and an empty list to hold confitmed users
# unconfirmed_users = ['alice', 'brian', 'candance']
# # confirmed_users = []
# today = {'programing', 'finanse', 'solopreneur','language','activity'}
# tomorow = []
#
# while today:
#     things_to_do = today.pop()
#     print(f"Tasks today: {things_to_do.title()}")
#     tomorow.append(things_to_do)
# print("\nThe following tasks are confirmed:")
# for task in tomorow:
#     print(task.title())
    #     confirmed_users.append(current_user)
# Verify each user until there are no more unconfirmed users.
# Move each verfied user into the list of confirmed users
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)
#     # Display all confirmed users
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# # removing All Instances of Specific Values from a list
# tools =['screw driver', 'file','screw driver','accu','file', 'accu' ]
# print(tools)
# while 'file' in tools:
#     tools.remove('file')
#
# print(tools)
# # Filling a Dictionary with User Prompt
#
# responses ={}
# # Set a flag to indicate that polling is active.
# polling_active = True
#
# while polling_active:
#     # Prompt for person's name and response.
#     name = input("\nWhat is your name? ")
#     response = input("Whitch mountain would you like to climb someday")
#     # Store the response in the tictionary.
#     responses[name] = response
#     # Find out if anyone else is going to take the poll
#     repeat = input("Would you like to let another person respond? (yes/no)")
#     if repeat == 'no':
#         polling_active = False
#         # Polling is complete. Show the results.
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")
#
# #  7-8
# sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
# finished_sandwiches = []
#
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print("I'm working on your " + current_sandwich + " sandwich.")
#     finished_sandwiches.append(current_sandwich)
#
# print("\n")
# for sandwich in finished_sandwiches:
#     print("I made a " + sandwich + " sandwich.")
#
# # 7-9
# sandwich_orders = [
#     'pastrami', 'veggie', 'grilled cheese', 'pastrami',
#     'turkey', 'roast beef', 'pastrami']
# finished_sandwiches = []
#
# print("I'm sorry, we're all out of pastrami today.")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
#
# print("\n")
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print("I'm working on your " + current_sandwich + " sandwich.")
#     finished_sandwiches.append(current_sandwich)
#
# print("\n")
# for sandwich in finished_sandwiches:
#     print("I made a " + sandwich + " sandwich.")
#
# # 7-10
# name_prompt = "\nWhat's your name? "
# place_prompt = "If you could visit one place in the world, where would it be? "
# continue_prompt = "\nWould you like to let someone else respond? (yes/no) "
#
# # Responses will be stored in the form {name: place}.
# responses = {}
#
# while True:
#     # Ask the user where they'd like to go.
#     name = input(name_prompt)
#     place = input(place_prompt)
#
#     # Store the response.
#     responses[name] = place
#
#     # Ask if there's anyone else responding.
#     repeat = input(continue_prompt)
#     if repeat != 'yes':
#         break
#
# # Show results of the survey.
# print("\n--- Results ---")
# for name, place in responses.items():
#     print(name.title() + " would like to visit " + place.title() + ".")
x = 6
y = 4
print(x ** y)