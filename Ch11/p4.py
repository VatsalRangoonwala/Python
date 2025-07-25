# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        real = self.r*c2.r - self.i*c2.i
        img = self.r*c2.i + self.i*c2.r
        return Complex(real, img)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"

a = Complex(1,2)
b = Complex(4,3)

print(a+b)
print(a*b)