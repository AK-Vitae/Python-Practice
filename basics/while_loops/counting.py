current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
print("\n")

# Letting the User Choose When to Quit
prompt = "Tell me a number, and I will count to that number from 1:"
prompt += "\nEnter 0 to end the program. "
number = 1
while number != 0:
    number = int(input(prompt))
    for count in range(1, number + 1):
        print(count)
    print("\n")
print("Thank you for your time")
print("\n")

# Using a Flag
prompt = "Tell me a number, and I will count to that number from 1:"
prompt += "\nEnter 0 to end the program. "
active = True  # flag acts as a signal for the program
while active:
    number = int(input(prompt))
    if number == 0:
        active = False
        print("Thank you for your time")
    else:
        for count in range(1, number + 1):
            print(count)
        print("\n")

#  Using break to Exit a Loop
prompt = "\nPlease enter your favorite number (Enter 'quit' when you are finished.): "
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(f'{message} is a fantastic number')
print("\n")

#  Using continue in a Loop
current_number = 0
prompt = "Please enter a number and I will print out all the preceding odd numbers: "
number = int(input(prompt))
while current_number < number:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
