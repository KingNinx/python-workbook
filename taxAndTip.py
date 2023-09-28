print("This is a tax and tip calculator")
print("Default tax rate included in this program is at 2.5%")
print("While the tip is 18% of the total amount before taxes.")
print("=============================")

taxRate = 0.025
tipRate = 0.18

mealCost = int(input("How much is the cost of your meal in dollars? "))
taxTotal = mealCost * taxRate
tipTotal = mealCost * tipRate

sumTotal = mealCost + taxTotal + tipTotal

print("Meal cost: $%.2f" % mealCost)
print("Tax is: $%.2f" % taxTotal)
print("Tip is: $%.2f" % tipTotal)
print("=============================")
print("Sum Total is: $%.2f" % sumTotal)
