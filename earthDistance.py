import math

t1 = float(input("Input latitude Point 1: "))
g1 = float(input("Input longitude Point 1: "))
t2 = float(input("Input latitude Point 2: "))
g2 = float(input("Input longitude Point 2: "))


def main(t1, g1, t2, g2):
    radius = 6371

    # convert latitude and longitude to radians
    t1 = math.radians(t1)
    g1 = math.radians(g1)
    t2 = math.radians(t2)
    g2 = math.radians(g2)

    formula = math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1)
                        * math.cos(t2) * math.cos(g1 - g2))

    distance = 6371.01 * formula
    return distance


distance = main(t1, g1, t2, g2)
print("The distance between the points is %.2f kilometers." % distance)
