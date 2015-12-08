def Number_game():
    from random import randint

    progress = 'y'
    guess = 0
    start_value = 6

    user_name = raw_input('Enter your name please.')

    while progress == 'y': 
        guess = int(input('Guess a number beetween 1 and 20 %s' % user_name))
        randomnumb = randint(0, 20) 
    
        if guess <= 0 or guess > 20: 
            print('Please enter a valid number for this game.')
            continue # start over
        
        while start_value > 0:
            if guess == randomnumb:
                print('Guessed right, with only %s guesses left!' % start_value)
                break
            if guess < randomnumb:
                print('Too low')
                start_value -= 1
            if guess > randomnumb:
                print('Too high')
                start_value -= 1
            if start_value == 0:
                print("You've failed me, BEGONE.")
                
        progress = raw_input('try again? y/n?')

Number_game()
