# List Methods

numbers = [5, 2, 1, 2, 4, 2, 7, 3]

print("Print original numbers array")
print(numbers)

print("Copy the numbers array to new numbers_2 array and print numbers_2")
numbers_2 = numbers.copy()
print(numbers_2)

print("Append 10 to the end of the numbers array and print")
numbers.append(10)
print(numbers)

print("Sort and print the numbers array")
numbers.sort()
print(numbers)

print("Reverse and print numbers in array")
numbers.reverse()
print(numbers)

print("Remove 5 and print new array")
numbers.remove(5)
print(numbers)

print("Count and print how many 2s")
count = numbers.count(2)
print(count)

print("Print True if 2 exists in the array")
two = print(2 in numbers)
