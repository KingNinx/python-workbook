cpToonie = 200
cpLoonie = 100
cpQuarter = 25
cpDime = 10
cpNickel = 5

cents = int(input("How many cents?: "))

toonies = cents // cpToonie
cents = cents % cpToonie

loonies = cents // cpLoonie
cents = cents % cpLoonie

quarters = cents // cpQuarter
cents = cents % cpQuarter

dimes = cents // cpDime
cents = cents % cpDime

nickels = cents // cpNickel
cents = cents % cpNickel

pennies = cents

print("Toonies:", toonies)
print("Loonies:", loonies)
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)

