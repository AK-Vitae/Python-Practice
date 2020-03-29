with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())
print("\n")

# Reading line by line
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
print("\n")

# Making a list of lines from a File
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()  # readlines() method takes each line from the file and stores it in a list
print(lines)
for line in lines:
    print(line.rstrip())
print("\n")

# Working with a File's Contents
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(f"The amount of characters in this text: {len(pi_string)}")
