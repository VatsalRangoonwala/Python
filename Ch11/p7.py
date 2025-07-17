# Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return f"Vector({self.n})"
    
    def __add__(self, v2):
        result = []
        if len(self.n) != len(v2.n):
            raise ValueError("Vectors must have same dimensions for addition.")
        for i in range(len(self.n)):
            sum = self.n[i] + v2.n[i]
            result.append(sum)
        return Vector(result)
    
    def __mul__(self, v2):
        result = 0
        if len(self.n) != len(v2.n):
            raise ValueError("Vectors must have same dimensions for dot(.) product")
        for i in range(len(self.n)):
            result = result + (self.n[i] * v2.n[i])
        return result
    
    def __len__(self):
        return len(self.n)
    
    
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(len(v1))
print(v1 + v2)
print(v1*v2)