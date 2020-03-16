name = input("Please enter your name: ")
print(f'\nHello, {name}!')

prompt = "If you tell us who you are, we can personalize the messages you see."
print("\n")
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f'\nHello, {name}!')
print("\n")

age = input("How old are you? ")
age = int(age)
greeter_age = 23
print(f'Oh interesting, you are {age} years old.')
if age < greeter_age:
    print(f"I am older than you by {greeter_age - age} years.")
elif age > greeter_age:
    print(f"You are older than me by {age-greeter_age} years.")
else:
    print("We are the same age!")
