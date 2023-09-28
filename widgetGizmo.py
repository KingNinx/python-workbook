print("A widget weighs 75 grams")
print("A gizmo weighs 112 grams")
print("This program allows to compute for the total weight in grams for all widgets and gizmos.")
print("===========================")

widget = 75
gizmo = 112

wid_amount = int(input("Enter amount of widgets: "))
giz_amount = int(input("Enter amount of gizmos: "))

total = widget * wid_amount + gizmo * giz_amount

print("The total weight in grams is:", total)
