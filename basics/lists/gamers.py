gamers = ['alex', 'james', 'david', 'emily']
for gamer in gamers:  # loop to print out each name in the list
    print(gamer)

for gamer in gamers:
    print(f"{gamer.title()}, that was a great move!")
    print(f"I can't wait to see your next match, {gamer.title()}.\n")
print("Thanks for everyone for participating!")
