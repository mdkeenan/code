# Single quotes wont work for a string with quotes: 
# course = 'Python's Course'
# Use double quotes instead:
course = "Python's Course"

first = 'John'
last = 'Smith'

# Define strings with carriage returns:
message = '''
Hello,

This is a message for you

Thank you,
Support
'''

print(message)

# Get the first character in string:
print(course[0])

# Get last character in string:
print(course[-1])

# Get characters from 0 to 3
print(course[0:3])

# Get characters from 1 to the end
print(course[1:])

# Use formatted strings to deal with special charactrs such as []:
# Prefix string with f and use curly braces to call a variable:
msg = f'{first} [{last}] is a coder'
print(msg)
