class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Fill up the gas tank"""
        print(f"This car has been filled with fuel")


# Inheritance

# Instances as attributes
class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            battery_range = 260
        elif self.battery_size == 100:
            battery_range = 315
        print(f"This car can go about {battery_range} miles on a full charge")

    def upgrade_battery(self):
        """Check if the battery size and set the capacity to 100"""
        if self.battery_size < 100:
            self.battery_size = 100


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parents class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        # The super() function is a special function that allows you to call a method from the parent class.
        self.battery = Battery(75)

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery}-kWh battery.")

    # Overriding Methods from the Parent Class
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")


# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.fill_gas_tank()
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()
