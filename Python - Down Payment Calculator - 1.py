# Python Down Payment Calculator

# Set the house_price variable to 1,000,000 dollars.
house_price = 1000000

# Set the good_credit boolean variable to True or False.
good_credit = True

# Use an if statement to determine how much the down payment must be depending on the buyers credit (good_credit variable) being set to True or False.

# Example A: This example uses print functions directly inside of the if statement. We must use the str function in order to convert (house_price * 0.10) and (house_price * 0.20) to a string value so that we can concatenate the value with the string "You must put down" and "dollars". Finally, depending on if good_credit is True or False we output the value of the down payment.
if good_credit:
    print("You must put down " + str(house_price * 0.1) + " dollars")
else:
    print("You must put down " + str(house_price * 0.2) + " dollars")

# Example B: This example sets the value of the down_payment variable inside of the if statement but waits to print the value of the down payment until until the if statement is complete. Finally, depending on if good_credit is True or False we output the value of the down payment. Note that we must use the "Literal String Interpolation" operator to format everything after "f" as a string since, by default, we can't concatenate strings and numeric values together in a print function.
if good_credit:
    down_payment = 0.1 * house_price
else:
    down_payment = 0.2 * house_price

print(f"You must put down {down_payment} dollars")
