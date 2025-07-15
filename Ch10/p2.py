# Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self, n):
        self.n = n
        print(f"The square of {self.n} is: {self.n**2}")
        print(f"The square root of {self.n} is: {self.n**(1/2)}")
        print(f"The cube of {self.n} is: {self.n**3}")
    
Calculator(4)