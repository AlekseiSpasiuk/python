class Complex:
    def __init__(self, real, i):
        self.real = real
        self.i = i

    def __add__(self, other):
        real = self.real + other.real
        i = self.i + other.i
        return Complex(real, i)

    def __mul__(self, other):
        real = self.real * other.real - self.i * other.i
        i = self.real * other.i + self.i * other.real
        return Complex(real, i)

    def __str__(self):
        return f"{self.real} + {self.i}i"

a = Complex(1, 1)
b = Complex(-1, -1)

print(a, b)
print(a + b)
print(a * b)



