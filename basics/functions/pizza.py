# Passing an Arbitrary Number of Arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("\n")


# Using Arbitrary Keyword Arguments
def build_customer(first, last, **customer_info):
    """Build a dictionary containing everything we know about a user."""
    customer_info['first_name'] = first
    customer_info['last_name'] = last
    return customer_info


customer = build_customer('frank', 'spitz', location='new york city', diet='vegetarian')
print(customer)
print("\n")