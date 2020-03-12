firstName = "john"
lastName = "smith"
fullName = f"{firstName} {lastName}"
age = 24.5
print(len(fullName))  # length of string, includes white space
print(fullName)
print(f"\n{fullName}")  # new line
print(f"\t{fullName}")  # tabbed line
print(fullName.split())  # creates list out of string
print(f"Hello, {fullName.title()}!")
print(f"Your age is:{age:10.4f}")  # formats floating point output to 4 decimal spaces
