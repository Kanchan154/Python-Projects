class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def showValue(self):
        print(f"The price of car of the {self.brand} is {self.price}")
        
# creating objects
obj1 = Car("Hundai", 1000000)
obj2 = Car(4000000, "Alto")


# obj1.showValue()
# obj2.showValue()
print(obj1.price)

# encapsulation
