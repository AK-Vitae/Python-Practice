# Large Files
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.read()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(f"{pi_string[:52]}...")
print(f"The number of characters in {filename}: {len(pi_string)}")

# Is your birthday contained in pi?
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.read()
pi_string = ''
for line in lines:
    pi_string += line.strip()
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")