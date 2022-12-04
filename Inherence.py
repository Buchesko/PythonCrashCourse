# Inherence
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
# Instances as atributes
class Battery:
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=75):
        """Initialize the battery's attribiutes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size """
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Print a statment about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspect of a car, specyfic to electric vechicle"""
    def __init__(self,make ,model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specyfic to an electric car"""
        super().__init__(make, model, year)
        # self.battery_size = 75
        self.battery = Battery()



    def describe_battery(self):
        """Print a statment describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh bttery")

    def fill_gas_tank(self):
        """Electric cars don't have gas tank"""
        print("This car doesn't need a gas tank!")
#
# my_tesla = ElectricCar('tesla','model s', '2019')
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# my_used_car = Car('subaru','outback', 2015)
# print(my_used_car.get_descriptive_name())
# my_tesla.describe_battery()

# my_used_car.update_odometr(23_500)
# my_used_car.read_odometr()
#
# my_used_car.increment_odometr(100)
# my_used_car.read_odometr()
#
# my_new_car = Car('audi','a4',2019)
# print(my_new_car.get_descriptive_name())
# # Modifying an Atribute's Value Directly
# my_new_car.update_odometr(9)
# # my_new_car.read_odometr()

# Try it yourselfe
"""9-6"""
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


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


# big_one = IceCreamStand('The Big One')
# big_one.flavors = ['vanilla', 'chocolate', 'black cherry']
# big_one.open_restaurant()
# big_one.describe_restaurant()
# big_one.show_flavors()


"""9-7"""
class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

#
# eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
# eric.describe_user()
#
# eric.privileges = [
#     'can reset passwords',
#     'can moderate discussions',
#     'can suspend accounts',
#     ]
#
# eric.show_privileges()