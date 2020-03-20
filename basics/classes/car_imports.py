# Importing a single class
from basics.classes.car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print("\n")

# Importing Multiple Classes from a Module
from basics.classes.electric_car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
print("\n")

# Importing an Entire Module
import basics.classes.electric_car

my_camaro = basics.classes.electric_car.Car('chevrolet', 'camaro', 2019)
print(my_camaro.get_descriptive_name())
my_rivian = basics.classes.electric_car.ElectricCar('rivian', 'R1T', 2020)
print(my_rivian.get_descriptive_name())
print("\n")

# Importing All Classes from a Module
from basics.classes.electric_car import *

my_civic = Car('honda', 'civic', 2019)
print(my_civic.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2019)
print(my_leaf.get_descriptive_name())
print("\n")

# Using Aliases
from basics.classes.electric_car import ElectricCar as EC

my_bolt = EC('chevy', 'bolt', '2019')
print(my_bolt.get_descriptive_name())
