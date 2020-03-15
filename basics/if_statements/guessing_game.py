guesses = [23, 1, 54, 43, 21, 59]
answer = 59
for guess in guesses:  # if-else if-else
    if guess < answer:
        print(f'You are {answer - guess} under')
    elif guess > answer:
        print(f'You are {guess - answer} over')
    else:
        print('Wow you finally got it right')
