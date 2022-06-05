# Comparison Operators

# Define variables
temp = 15
name = "Mike"

# Use the len function to count the number of characters in name and assign the numeric value to the name_count variable.
name_count = (len(name))

# Print the contents of the name_count variable.
print(name_count)

# Using the EQUAL (==) comparison operator determine if temp is equal to 15. If it is then print "The temperature is 15 degrees celsius". Otherwise, if it is not then print "The temperature is NOT 15 degrees celsius".
if temp == 15:
    print("The temperature is 15 degrees celsius")
else:
    print("The temperature is NOT 15 degrees celsius")

# Using the NOT EQUAL (!=) comparison operator determine if temp is NOT equal to 15. If it is NOT then print "The temperature is NOT 15 degrees celsius". Otherwise, if it is then print "The temperature is 15 degrees celsius".
if temp != 15:
    print("The temperature is NOT 15 degrees celsius")
else:
    print("The temperature is 15 degrees celsius")

# Using the greater than (>) comparison operator determine if temp is greater to 15. If it is then print "It's a hot day". If it is less than 10 then print "It's a cold day". Otherwise, print "It's neither hot nor cold".
if temp > 30:
    print("It's a hot day")
elif temp < 10:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")

# Using the less than "<" comparison operator determine if the number of characters in the name_count variable is less than 3. If it is then print "Name must be at least 3 characters long"
if name_count < 3:
    print("Name must be at least 3 characters long")
elif name_count > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")
