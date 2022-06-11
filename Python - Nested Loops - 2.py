# Nested Loops

# Print the following using nested loops (without the #s):

# xxxxx
# xx
# xxxxx
# xx
# xx

numbers = [5, 2, 5, 2, 2]
y = ''

# Traditional programming way
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

# Python nuanced
for count in numbers:
    print('x' * count)
