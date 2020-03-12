shoes = ['nike', 'reebok', 'adidas', 'puma']
print(shoes)
print(shoes[0])
print(shoes[0].title())
print(shoes[-1])
message = f"My first shoe brand was {shoes[0].title()}."
print(message)

# Adding to a list
shoes.append('fila')
print(shoes)
shoes = []  # Adding elements to an empty list
shoes.append('nike')
shoes.append('reebok')
shoes.append('adidas')
shoes.append('puma')
print(shoes)

# Inserting into a list
shoes.insert(0, 'fila')
print(shoes)

# Removing an item from a list
del shoes[0]
print(shoes)
popped_shoe = shoes.pop() # "pops" off last item in list
print(shoes)
print(popped_shoe)
print(f"The last shoe I owned was a {popped_shoe.title()}.")
first_owned = shoes.pop(0)
print(f"The first shoe I owned was a {first_owned.title()}.")
shoes = ['nike', 'reebok', 'adidas', 'puma']
print(shoes)
shoes.remove('reebok')
print(shoes)
