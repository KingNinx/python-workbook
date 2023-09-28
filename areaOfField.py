sqftPerAcre = 43560

a = float(input("What is the length of the field? "))
b = float(input("What is the width of the field? "))
c = a * b / sqftPerAcre

print("The area of the field is", c, "acres")
