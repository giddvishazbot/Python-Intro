# this is the same as choose_color.py except it adheres to PEP8 standards
def choose_color():
    while True:
        try:
            choice = int(input('Choose a number beetween 0 and 36: '))
        except KeyboardInterrupt:
            return # void function, returns no value
        except:
            continue # jump to the end of the loop and loop again

        if choice not in range(0, 37):
            print('Not a valid number')
            continue

        g = 0
        r = range(1, 11, 2)+range(12, 19, 2)+range(19, 29, 2)+range(30, 37, 2)
        b = [x for x in range(1, 37) if x not in r]

        if choice == g:
            print('You got green')
        if choice in b:
            print('You got black')
        if choice in r:
            print('You got red')

        try:
            play_again = raw_input('Pick again? (y/n): ') == 'y'
        except:
            return
        if not play_again:
            return

choose_color()
