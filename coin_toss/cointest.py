from random import randint


progress = 'y'
guess = 0



while progress == 'y': 
    guess = int(input('Guess Heads or tails for a cointoss.(1 =heads, 2= tails,)'))
    cointoss = randint(1, 2)

    if guess is not cointoss:
        print('Guessed wrong, too bad,')
    else:
        print('Guessed right, nicejob,')

    progress = raw_input('try again? y/n?')