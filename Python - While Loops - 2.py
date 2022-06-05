# Guessing Game

# Instantiate the variables with values.
guess_count = 0
guess_number = 0
guess_limit = 3
Secret_number = 9

# Example A
# While guess_count is less than 3 AND guess_number is not equal to 9.
while guess_count < guess_limit and guess_number != 9:
    # Ask the user to input a number by saying "Guess:" and assign that number to guess_number.
    # Whatever the user types into the terminal it will be interpreted as text so in order to use it in arithmetic we use the int manipulator to change it to an integer from a string.
    guess_number = int(input("Guess:"))
    # Increment the guess_count variable by one.
    guess_count += 1
    # If guess_number is equal to 9 print the congrats text and since we have satisfied the requirement above making guess_number equal to 9 it stops the while loop.
    if guess_number == Secret_number:
        print("Congrats, you guessed the correct number!")
        break
    # This will only run if the user did not input 9 yet. If the guess_number variable does not equal 9 print the sorry text.
    elif guess_number != Secret_number:
        print("Sorry, wrong number.")
    # This will only run if the user did not input 9 yet. If the guess_count variable is equal to 3 then print the sorry text.
    if guess_count == guess_limit:
        print("Sorry, you failed to guess the correct number.")

# Example B
# The only difference from A is that here the break statement is used and the top level comparison is different.
while guess_count < guess_limit:
    guess_number = int(input("Guess:"))
    guess_count += 1
    if guess_number == Secret_number:
        print("Congrats, you guessed the correct number!")
        # The break statement stops the loop if the argument before it is true.
        break
    elif guess_number != Secret_number:
        print("Sorry, wrong number.")
    if guess_count == guess_limit:
        print("Sorry, you failed to guess the correct number.")
