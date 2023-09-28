a = float(input("Please input amount in your savings: "))
interest = 1 + 0.04

yearOne = a * interest
yearTwo = yearOne * interest
yearThree = yearTwo * interest


print("The amount on your savings with interest on year 1 is: $%.2f." % yearOne)
print("The amount on your savings with interest on year 2 is: $%.2f." % yearTwo)
print("The amount on your savings with interest on year 3 is: $%.2f." % yearThree)
