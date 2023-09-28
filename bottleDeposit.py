lessDeposit = 0.10
moreDeposit = 0.25

less = int(input("How many bottles are 1 liter or less? "))
more = int(input("How many bottles are more than 1 liter? "))

totalRefund = less * lessDeposit + more * moreDeposit

print("Your total refund amount will be $%.2f." % totalRefund)
