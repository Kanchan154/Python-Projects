from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     # def sound():
#     #     print("Dog makes sound")
#     def eat(self):
#         print("Dog can eat")

# class Labra(Dog):
#     def sound(self):
#         print("Labra makes sound")

# labra = Labra()
# labra.eat();  
# labra.sound()


# Shape area calculator
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Ractangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        print(f"Area of Ractangle is: {self.l * self.w}")

class Square(Shape):
    def __init__(self, s):
        self.s = s
    def area(self):
        print(f"Area of Square is: {self.s ** 2}")
    
class triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        print(f"Area of Triangle is: {self.h * self.b * 0.5}")

tri = triangle(b=20, h=10)
sq = Square(s=5)
ract = Ractangle(10,20)

tri.area()
sq.area()
ract.area()

