# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    def __init__(self):
        print("I am an animal")

class Pets(Animals):
    def __init__(self):
        super().__init__()
        print("Everyone is loving me when i am their pet")

class Dog(Pets):
    def __init__(self):
        super().__init__()

    def bark(self):
        print("I can speak in my language like bow bow")


a = Dog()
a.bark()