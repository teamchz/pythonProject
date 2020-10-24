''' Create class
class Customer:
    name = ""
    last_name = ""
    age = 0

    def add_cart(self):
        print("Add to cart", self.name, self.age)


customer1 = Customer()
customer1.name = "Team"
customer1.age = 50

customer2 = Customer()
customer2.name = "Boom"
customer2.age = 16

customer1.add_cart()
customer2.add_cart()
'''

class Vehical:
    license_code = ""
    serial_code = ""

    def turn_on_air(self):
        print("Turn on Air!")


class Van(Vehical):
    def Fly(self):
        print("Let Fly!")

van1 = Van()
van1.turn_on_air()
van1.Fly()