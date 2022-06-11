# List Methonds

# Remove all duplicate numbers from numbers array and print them to the screen.

numbers = [5, 2, 1, 2, 4, 2, 7, 3]
uniques = []


for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
