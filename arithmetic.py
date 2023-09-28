from math import log10

a = int(input("Input value of A: "))
b = int(input("Input value of B: "))

print(a, "+", b, "is", a + b)
print(a, "-", b, "is", a - b)
print(a, "*", b, "is", a * b)
print(a, "/", b, "is", a / b)
print(a, "%", b, "is", a % b)
print("The base 10 logarithm of", a, "is", log10(a))
print(a, "to the power of", b, "is", a ** b)
