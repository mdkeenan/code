# Weight Converter

# Ask user for input and assign to variables. Ensure that the weight variable is converted to a float type value (fraction) instead of a string (text) so that we can use it for calculations later.
weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ")

# If the user selects L for pounds convert it to kilograms by multiplying it by 0.45 and assign it to the your_weight variable then print value of your_weight. Make sure to use the upper method to ensure that L is converted to uppercase in case the user uses lowercase.
if unit.upper() == "L":
    your_weight = weight * 0.45
    print(f"You are {your_weight} kilograms.")
# If user selects K for kilograms convert it to pounds by dividing it by 0.45 and assign it to the your_weight variable then print the value of your_weight. Make sure to use the upper method to ensure that K is converted to uppercase in case the user uses lowercase.
elif unit.upper() == "K":
    your_weight_kg = weight / 0.45
    print(f"You are {your_weight_kg} pounds")
# Otherwise, if user selects neither L or K then print "Must use L or K".
else:
    print("Must use L or K")
