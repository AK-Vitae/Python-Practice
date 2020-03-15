fav_toppings = ['mushrooms', 'onions', 'pineapples', 'chicken']

# if-else
for fav_topping in fav_toppings:
    if fav_topping == 'onions':
        print(f'{fav_topping.title()}, I think I will skip on those today')
    else:
        print(f'{fav_topping.title()}, extra please')

for fav_topping in fav_toppings:
    if fav_topping != 'chicken':  # != means not equals
        print(f'Hold the {fav_topping}!')

bad_toppings = ['peppers', 'anchovies', 'olives']
requested_topping = 'pepperoni'
if requested_topping not in bad_toppings:
    print(f'Luckily we have {requested_topping.title()} for you today')

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
print("\nFinished making your pizza!")

# Checking for special items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# Checking that a list is not empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")
