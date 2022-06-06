# For Loops

# This is just for readability. Adds a space before and after each example.
spc = '\r\n'

print(spc + 'Example A' + spc)
# Print all of the characters in 'Python'
for thingy in 'Python':
    print(thingy)

print(spc + 'Example B' + spc)
# Print the array of things.
for thingy in ['Mike', 'John', 'Sarah']:
    print(thingy)

print(spc + 'Example C' + spc)
# Print from 0 to 3.
for thingy in range(4):
    print(thingy)

print(spc + 'Example D' + spc)
# Print from 4 to 5.
for thingy in range(4, 6):
    print(thingy)
    
print(spc + 'Example D' + spc)
# Print from 4 to 8 in increments of 2.
for thingy in range(4, 9, 2):
    print(thingy)
