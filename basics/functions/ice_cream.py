def get_ice_cream(size, flavor, *toppings):
    """Summarize the ice cream we are about to get."""
    print(f"\nGetting a {size} {flavor} ice cream cone with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
