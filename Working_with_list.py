# # # looping through entire list
# magicans = ['alice', 'david', 'carolina']
# for magican in magicans:
#     print(f"{magican.title()}, that was great trick")
#     print(f"I can't wait to see your next trick, {magican.title()}.\n")
# print(f"Thank you, everyone. that was a great magic show")
# print(magicans)

# Numerical List
# for value in range(1,5):
#     print(value)
# #     use range() to make a list of numbers
# numbers = list(range(1,6))
# print(numbers)
# # liczby parzyste
# even_numbers = list(range(2,11,2))
# print(even_numbers)
# #  first 10 squer numbers
# squeres = []
# # for value in range(1,11):
# #     squere = value ** 2
# #     squeres.append(squere)

# for value in range(1 ,11):
#     squeres.append(value ** 2)
#
# squeres = [value**2 for value in range(1,11)]
#
# print(squeres)

# Excersis
# couting 20
# numbers = [value++1 for value in range(0,20)]
# print(numbers)
# One Milion
# numbers = [number++1 for number in range (0,10000)]
# print(numbers)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# # odd number
# list_odd = [number++1 for number in range(1,1000000)]
# only_odd = [num for num in list_odd if num % 2 == 1]
# print(only_odd)
