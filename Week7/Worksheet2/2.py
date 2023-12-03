from random import randrange


mainloop = True
while mainloop:
    start = True
    guess_num = randrange(1, 11)
    cycle = 0
    print('--Welcome to the Guessing game!--')
    print("I've chosen a number between 1 and 10 - Try to guess it!")
    print()
    while start:
        cycle += 1
        if cycle > 10:
            print('Wow! You are 5 y.o. How did you managed to start the program than?!')
        print(f'---Round {cycle} - GUESS!!!---')
        try:
            guess = int(input('Type your guess: '))
            if guess == guess_num:
                print('YOU DID IT! YOU WON!')
                start = False
            elif guess < guess_num:
                print('Try bigger....')
            else:
                print('Try smaller...')

        except ValueError:
            print("C'mon! It must be an integer number!")
        print()
    if not start:
        print(f'---Your score - {cycle} points!---')
        print()
        a = input('Do you want to try again? (y/n): ')
        if a == 'y':
            pass
        elif a == 'n':
            mainloop = False
        else:
            print('What did you mean? Get out of the game!')
            mainloop = False