dog_0 = {'breed': 'shiba inu', 'age': 5}
print(dog_0['breed'].title())
print(dog_0['age'])

# Accessing Values in a Dictionary
birthday = dog_0['age'] + 1
print(f'Your dog will turn {birthday} next week!')

# Adding New Key-Value Pairs
print(dog_0)
dog_0['fur color'] = 'black and tan'
dog_0['weight'] = 30
print(dog_0)

# Modifying Values in a Dictionary
print(dog_0)
dog_0['weight'] = 28
print(f"Your {dog_0['breed'].title()} is now {dog_0['weight']} lbs.")

dog_0 = {'x_position': 0, 'y_position': 25, 'speed': 'slow'}
print(f"Dog's starting position in this game of fetch: {dog_0['x_position']}")
if dog_0['speed'] == 'slow':
    x_increment = 1
elif dog_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
dog_0['x_position'] = dog_0['x_position'] + x_increment
print(f"New position of dog is {dog_0['x_position']}")

# Removing Key-Value Pairs
print(dog_0)
del dog_0['y_position']
print(dog_0)

# Using get() to Access Values
dog_0 = {'breed': 'shiba inu', 'age': 5}
# The get() method requires a key as a first argument.
# As a second optional argument, you can pass the value to be returned if the key does not exist.
weight = dog_0.get('weight', 'No weight recorded')
print(weight)

# A List of Dictionaries
dog_0 = {'breed': 'shiba inu', 'age': 5}
dog_1 = {'breed': 'husky', 'age': 3}
dog_2 = {'breed': 'golden retriever', 'age': 7}
dogs = [dog_0, dog_1, dog_2]
for dog in dogs:
    print(dog)

# A List in Dictionary
dog_food = {
    'protein': 'chicken',
    'vegetables': ['carrots', 'green beans', 'potatoes']
}
print(f"You bought {dog_food['protein']} kibble "
      "with the following vegetables:")
for vegetable in dog_food['vegetables']:
    print("\t" + vegetable)
