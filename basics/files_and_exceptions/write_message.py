# Writing to an empty file
filename = 'programming.txt'
with open(filename, 'w') as file_object:  # the 'w' tells Python that we want to open the file in write mode
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")

# Appending to a file
filename = 'programming.txt'
with open(filename, 'a') as file_object:  # 'a' argument to open the file for appending
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
