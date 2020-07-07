class Restaurant():

    def __init__(self, name, cuisine_type):
        # Initalize the restaurant
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaruant(self):
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        print("the MF'n restaurant is open brooooo")

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type='ice cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors: ")    
        for flavor in self.flavors:
            print("- " + flavor.title())


big_freeze = IceCreamStand('The Big Freeze')
big_freeze.flavors = ['vanilla','chocolate','banana','raspberry','coconut','peach']
big_freeze.describe_restaruant()
big_freeze.show_flavors()
