# Import multiple classes from a Module
from Inherence import Restaurant,Car

# Import entire moduls
import  Inherence

my_beatle = Inherence.Car('Volkswagen','beetle',2019)
print(my_beatle.get_descriptive_name())

my_tesla = Inherence.ElectricCar('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())


my_new_car = Car('Audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometr_reading = 23
my_new_car.read_odometr()

restaurant = Restaurant('Mc Donalds', 'fast food')
print(restaurant.describe_restaurant())

