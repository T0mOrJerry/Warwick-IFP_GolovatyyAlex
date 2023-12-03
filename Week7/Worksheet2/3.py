from random import choice

mainloop = True
with open('words.txt') as file:
    li = [i.strip().lower() for i in file.readlines()]
while mainloop:
    start = True
    guess_an = list(choice(li))
    guess_user = ['_' for i in range(len(guess_an))]
    cycle = 0
    mist = 5
    print('--Welcome to the Words Guessing Game!--')
    print("I've chosen an animal - try to guess it, by characters")
    print("You can have only 5 mistakes - than you will lose")
    print(f"The word is - {''.join(guess_user)}")
    print()
    while start:
        cycle += 1
        print(f'---Round {cycle} - GUESS!!!---')
        guess = input('Type your guess: ').lower()
        if guess in guess_an:
            for i in range(len(guess_an)):
                if guess_an[i] == guess:
                    guess_user[i] = guess
            if '_' not in guess_user:
                print('YOU DID IT! YOU WON!')
                start = False
                win = True
            else:
                print(f"Great! {''.join(guess_user)}")
        else:
            if mist == 0:
                print('Oops...')
                start = False
                win = False
            else:
                print('There is no such letter((')
                mist -= 1
                print(f'--{mist} mistakes left for you')
        print()
    if not start:
        if win:
            print(f'---It took - {cycle} turns!---')
        else:
            print("--It seems like you've lost--")
            print('LOOOOSER!!!!')
        print(f'The word was - {"".join(guess_an)}')
        print()
        a = input('Do you want to try again? (y/n): ')
        if a == 'y':
            pass
        elif a == 'n':
            mainloop = False
        else:
            print('What did you mean? Get out of the game!')
            mainloop = False
