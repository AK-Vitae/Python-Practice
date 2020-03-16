# Moving Items from One List to Another
unconfirmed_users = ['jSmith', 'jDoe', 'mPark', 'aJones']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop(0)
    print(f"Verifying user: {current_user}")
    confirmed_users.append(current_user)
print("\nThe following usernames have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)
print("\n")

# Removing All Instances of Specific Values from a List
unconfirmed_users = ['jSmith', 'jDoe', 'mPark', 'aJones', 'jPatel', 'jDoe', 'tJones']
print(unconfirmed_users)
while 'jDoe' in unconfirmed_users:
    unconfirmed_users.remove('jDoe')
print("jDoe as a username is already taken")
print(unconfirmed_users)
