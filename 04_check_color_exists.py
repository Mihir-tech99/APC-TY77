# Program 4: Check whether a color exists
colors = ("Red", "Green", "Blue", "Yellow", "Black")
color = input("Enter a color: ")

if color in colors:
    print("Color exists in the tuple.")
else:
    print("Color does not exist in the tuple.")
