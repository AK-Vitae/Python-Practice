for value in range(1, 10):  # range() can be used to print a series of numbers
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))  # 3rd parameter in range specifies step size
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2  # ** represents exponents
    squares.append(square)
print(squares)

squares = []  # another way to run the loop above
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

squares = [value ** 2 for value in range(1, 11)]  # even more compact way of running the loop above
print(squares)

squares = [pow(value, 2) for value in range(1, 11)]  # using pow() to calculate exponents
print(squares)

# Basic statistics of a list of numbers without imports
print(min(squares))  # min
print(max(squares))  # max
print(sum(squares))  # sum
print(sum(squares) / len(squares))  # mean
