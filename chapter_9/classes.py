class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def decribe_restaurant(self):
        print(f"This restaurant is called {self.name} and its cuisine is {self.type}")

    def open_restaurant(self):
        print("The restaurant is open")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num


my_restaurant = Restaurant("Best", "barbec")

print(my_restaurant.name)
print(my_restaurant.type)
my_restaurant.decribe_restaurant()
my_restaurant.open_restaurant()

rest_1 = Restaurant("McBobs", "Hamburguer")
rest_2 = Restaurant("KingMC", "Big Hamburguer")
rest_3 = Restaurant("Another", "Very good")

rest_1.decribe_restaurant()
rest_2.decribe_restaurant()
rest_3.decribe_restaurant()

print(rest_1.number_served)
rest_1.set_number_served(5)
print(rest_1.number_served)
rest_1.increment_number_served(3)
print(rest_1.number_served)