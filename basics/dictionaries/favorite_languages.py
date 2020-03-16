# Looping Through All Key-Value Pairs
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():  # items() returns a list of key-value pairs
    print(f"{name.title()}'s favorite programming language is {language.title()}")

print("Python is GOAT, let's see who thinks otherwise")
for name, language in favorite_languages.items():
    print(f"{name.title()}, I see you like {language.title()}.")
    if language.title() != 'Python':
        print("\tYou have poor taste")
    else:
        print("\tYou have great taste")

# Looping Through All the Keys in a Dictionary
friends = ['jen', 'phil']
for name in favorite_languages.keys():  # keys() accesses key values
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping Through All Values in a Dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    # set() identifies the unique items in the list and builds a set from those items
    print(language.title())

# List in a Dictionary
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# A Dictionary in a Dictionary
programmers = {
    'jsmith': {
        'first': 'john',
        'last': 'smith',
        'location': 'New Jersey'
    },
    'jdoe': {
        'first': 'jane',
        'last': 'doe',
        'location': 'Texas'
    }
}
for username, user_info in programmers.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
