# single Level

def SingleLevelInhertance():
    class Animal:
        def eat(self):
            print("Animal can eat")
    class Dog(Animal):
        def bark(self):
            print("Animal can bark")
    
    animal = Animal()
    dog = Dog()
    
    animal.eat()
    dog.eat()
    dog.bark()
    
# SingleLevelInhertance()

# Multiple Inheritance
def multipleInheritance():
    class Parent1:
        def show(self):
            print("Parent 1 class")
    class Parent2:
        def show(self):
            print("Parent 2 class")
    class Child(Parent1, Parent2):
        def show(self):
            print("Child Class")

    child = Child()
    child.show()
# multipleInheritance()

# multi-level inheritance
def multiLevel():
    class Parent:
        def show(self):
            print("Parent class")
    class Child(Parent):
        def show(self):
            print("Child class")
    class GrandChild(Child):
        def show(self):
            print("Grand Child Class")
    gc = GrandChild()
    gc.show()
    
# multiLevel()

# heirarchial inheritance
def HierarchialInheritance():
    class Parent:
        def show(self):
            print("Parent class")
    class Child1(Parent):
        def show(self):
            print("Child-1 class")
    class Child2(Parent):
        # def show(self):
        #     print("Child-2 class")
        pass
    
        def show(self):
            print("Grand Child Class")
    child1 = Child1()
    child2 = Child2()
    child1.show()
    child2.show()
HierarchialInheritance()

# hybrid inheritance
def HybridInheritance():
    class Parent:
        def show(self):
            print("Parent class")
    class Child1(Parent):
        def show(self):
            print("Child-1 class")
    class Child2(Parent):
        def show(self):
            print("Child-2 class")
    class GC(Child2, Child1):
        pass
    
    gc1 = GC()
    gc1.show()
# HybridInheritance()
    