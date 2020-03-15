first_name = "john"
last_name = "smith"
full_name = f"{first_name} {last_name}"
age = 24.5
print(len(full_name))  # length of string, includes white space
print(full_name)
print(f"\n{full_name}")  # new line
print(f"\t{full_name}")  # tabbed line
print(full_name.split())  # creates list out of string
print(f"Hello, {full_name.title()}!")
print(f"Your age is:{age:10.4f}")  # formats floating point output to 4 decimal spaces
first_name = " john "
full_name.rstrip()  # removes white space right of String
full_name.lstrip()  # removes white space left of String
full_name.strip()  # removes white space on both sides of String
