def number_game(min, max, guesses):
    from random import randint
    
    username = greet_user()
    
    while True:
        correct = randint(min, max)
        remaining = guesses
        while remaining > 0:
            user_guess = guess(username, min, max)
            if check_guess(user_guess, correct, remaining):
                break
            remaining -= 1
            if (remaining == 0):
                print("You've failed me, BEGONE.")
            
        if try_again():
            remaining = guesses
        else:
            break


def greet_user():
    try:
        username = input('What is your name? ')
        assert len(username) > 0
    except KeyboardInterrupt:
        raise
    except:
        print("Oh, no? That's too bad!")
        username = 'Keith'
    print('Hello {}! Welcome to the number game.'.format(username))
    return username


def try_again():
    while True:
        try:
            try_again = input('Want to play again? (y/n) ').lower()
            if try_again not in ['y', 'n']:
                print("Please enter 'y' or 'n'")
                continue
            return try_again == 'y'
        except KeyboardInterrupt:
            raise
        except:
            raise


def guess(username, min, max):
    prompt = '{}, '.format(username)
    prompt += 'please enter a number between {} and {}: '.format(min, max)
    error_msg = 'Please enter a valid number for this game.'
    while True:
        try:
            guess = int(input(prompt))
            if guess not in range(min, max + 1):
                print(error_msg)
                continue
            return guess
        except KeyboardInterrupt:
            raise
        except:
            print(error_msg)

  
def check_guess(guess, correct, remaining_guesses):
    rg = int(remaining_guesses) - 1
    plural = '' if rg == 1 else 'es'
    if guess == correct:
        print('Guessed right, with only {} guess{} left!'.format(rg, plural))
        return True
        
    if guess < correct:
        print('Guessed too low')
    if guess > correct:
        print('Guessed too high')
    return False


number_game(0, 20, 6)
