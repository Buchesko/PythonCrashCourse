# Defining a function
# def greet_user():
#     """Display a simply greetings"""
#     print("Hello")
# greet_user()
# "Passing Information to a function"
# prompt = "Wprowadź nazwę użytkownika. Naciśnij q jak koniec"
# def greet_user(username):
#     while True:
#         username = input(prompt)
#         if username == 'q':
#             break
#         else:
#             print(f"Greetings {username.title()}")
# greet_user(username=True)
#

#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"\t I'd love to go to {city.title()}!\n")

# Making an Argument Optional

# def get_forrmated_name(first_name, middle_name, last_name):
#     """Return a full name neatly forrmated"""
#     if middle_name:
#         full_name= f"{first_name,middle_name, last_name}"
#     else:
#         full_name = f"{first_name,last_name}"
#     return full_name
# first_name = input("First name:")
# middle_name = input("Middle name: ")
# last_name = input("Last Name")
# musican = get_forrmated_name(first_name,middle_name,last_name)
# print(musican)

# """Returning a Dictionary """
#
# def build_person(first_name, last_name,age=None):
#     """Return a dictionary of information about a person"""
#     person = {'first':first_name,'last':last_name}
#     if age:
#         person['age'] = age
#     return person
# while True:
#     first_name = input("First name:")
#     last_name = input("Last Name")
#     if first_name =='q' or last_name=='q':
#         break
#     else:
#         musican = build_person(first_name,last_name,age=27)
#         print(musican)
#
#
# def make_album(artist, title, tracks=0):
#     """Build a dictionary containing information about an album."""
#     album_dict = {
#         'artist': artist.title(),
#         'title': title.title(),
#     }
#     if tracks:
#         album_dict['tracks'] = tracks
#     return album_dict
#
#
# # Prepare the prompts.
# title_prompt = "\nWhat album are you thinking of? "
# artist_prompt = "Who's the artist? "
#
# # Let the user know how to quit.
# print("Enter 'quit' at any time to stop.")
#
# while True:
#     title = input(title_prompt)
#     if title == 'quit':
#         break
#
#     artist = input(artist_prompt)
#     if artist == 'quit':
#         break
#
#     album = make_album(artist, title)
#     print(album)
#
# print("\nThanks for responding!")

# # Passing a list
# def great_users(names):
#     """Print a simple greetings to each users in the list."""
#     for name in names:
#         msg = f"Hello,{name.title()}!"
#         print(msg)
#
# usernames = ['hannah', 'ty', 'margot']
# great_users(usernames)

# Modifying a List in a Function
# Start with some designs that need to be printed.


# def print_models(unprinted_designs, completed_models):
#     """
#         Stimulate printing each design, until none are left
#     Move each design to comleted_models after printing
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
#
#
# def show_compleate_models(completed_models):
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
#
# unprinted_designs = ['phone case' ,'robot pendant', 'dodecahedron']
# completed_models = []
#
#
# print_models(unprinted_designs,completed_models)
# show_compleate_models(completed_models)


# Passing an Arbitrary Number of Arguments
#
# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested"""
#     print(toppings)
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a pizza with the following toppings: ")
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra chees')

#

# # Mixing Positional and Arbitrary Arguments
# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings: ")
#     for topping in toppings:
#         print(f"-{topping}")
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'muschrooms', 'green pappers', 'extra cheese')
#

# Arbitrary Keyword Arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user:"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstain',
                             location='princeton',
                             field='physics')
print(user_profile)