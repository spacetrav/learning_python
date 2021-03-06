class Car():
    """ attempt to represent a car using a class """

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you cant roll back the odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 300
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 70:
            self.battery_size = 85
            print("Upgraded battery to 85 kWh")
        else:
            print("The battery is already at the highest capacity")

class ElectricCar(Car):
    """ represents aspects of a car specific to electric vehicles """
    def __init__(self,make,model,year):
        """initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()


# my_tesla = ElectricCar('tesla','model s',2016)
# # print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()

# my_tesla.battery.upgrade_battery()
# my_tesla.battery.describe_battery()
# # my_tesla.battery.get_range()

# my_tesla.battery.upgrade_battery()
# my_tesla.battery.describe_battery()