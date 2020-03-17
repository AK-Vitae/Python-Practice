def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('john', 'lennon')
print(musician)
print("\n")


# Making an Argument Optional
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('tupac', 'amaru', 'shakur')
print(musician)
print("\n")


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted. Middle name is optional"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('john', 'lennon')
print(musician)

musician = get_formatted_name('tupac', 'shakur', 'amaru')
print(musician)


# Returning a Dictionary
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)


def get_formatted_name(first_name, last_name, time_of_day):
    """Return a full name, neatly formatted."""
    greeting = {'first': first_name, 'last': last_name, 'time': time_of_day}
    return greeting


while True:
    print("\nPlease tell me your name (enter 'q' at any time to quit): ")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    t_of_day = input("Is it morning, afternoon, or evening? (enter 'q' at any time to quit): ")
    if t_of_day == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name, t_of_day)
    print(f"Good {formatted_name['time'].lower()} {formatted_name['first']} {formatted_name['last']}")

print("\n")


# Passing a List
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
print("\n")


# Modifying a List in a Function
def invite(pending_invitations, invited):
    """Simulate the process of inviting people to a party, until there are no pending invitations"""
    while pending_invitations:
        current_invitation = pending_invitations.pop(0)
        print(f"Inviting: {current_invitation.title()}")
        invited.append(current_invitation.title())


def show_invited(invited):
    """Show all the people that were invited"""
    if len(invited) == 1:
        print("\nThe following person has been invited: ")
        print(invited[0])
    else:
        print("\nThe following people have been invited: ")
        for inv in invited:
            print(inv)


p_invitations = ['lance']
invs = []
invite(p_invitations, invs)
show_invited(invs)

p_invitations = ['lance', 'kane', 'olaf', 'samantha']
invs = []
invite(p_invitations[:], invs)  # The slice notation [:] makes a copy of the list to send to the function
show_invited(invs)
print(p_invitations)
