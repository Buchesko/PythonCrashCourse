# Creating and using class
#
# Creating the dog class
class Dog:
    """A simple attemp to model a dog"""
    def __init__(self, name ,age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is sitting.")

    def roll_over(self):
        """Simulate rolling over in response to acommand"""
        print(f"{self.name} rolled over")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)


print(f"My dog's name is {my_dog.name}")
print(f" My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"My dog's name is {your_dog.name}")
print(f"My dog is {your_dog.age} years old.")
my_dog.roll_over()

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2
class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

mean_queen = Restaurant('the mean queen', 'pizza')
mean_queen.describe_restaurant()

ludvigs = Restaurant("ludvig's bistro", 'seafood')
ludvigs.describe_restaurant()

mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restaurant()

# 9-3
class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()

# Working with Classes and instances
# """The Car Classes"""
class Car:
    """A simple attempt to represent a car"""
    def __init__(self,make,model,year):
        """Initialize attributes to describe a car,"""
        self.make = make
        self.model = model
        self.year = year
        # Setting defult value for an Atribute
        self.odometr_reading = 10

    def get_descriptive_name(self):
        """Return a neatly formmated descreptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometr(self):
        """Print a statment showing the car's milage"""
        print(f"This car has {self.odometr_reading} miles on it")
#     Modifying an Attribute' Value through a Metod
    def update_odometr(self,milage):
        """Set the odometr reading to the given value
        Rejectthe change if it attemps to roll the odometr back.
        """
        if milage >= self.odometr_reading:
            self.odometr_reading = milage
            print(milage)
        else:
            print("you can't rool back an odometr")

    def increment_odometr(self,miles):
        """Add the given amount to the odometr reading."""
        self.odometr_reading += miles

class ElectricCar(Car):
    """Represent aspect of a car, specyfic to electric vechicle"""
    def __init__(self,make ,model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla','model s', '2019')
print(my_tesla.get_descriptive_name())

my_used_car = Car('subaru','outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometr(23_500)
my_used_car.read_odometr()

my_used_car.increment_odometr(100)
my_used_car.read_odometr()

my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
# Modifying an Atribute's Value Directly
my_new_car.update_odometr(9)
# my_new_car.read_odometr()
# 9-4
class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 430
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(1257)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(239)
print(f"Number served: {restaurant.number_served}")