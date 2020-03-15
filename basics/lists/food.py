foods = ['pizza', 'fried chicken', 'pasta', 'tacos', 'ramen']
print(foods[0:3])
print(foods[:3])
print(foods[2:])

print("Here are my top 3 favorite foods:")
for food in foods[:3]:
    print(food.title())

friend_foods = foods[:]  # Copying a list
print("My favorite foods are:")
print(foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
