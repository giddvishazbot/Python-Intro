def choose_color():
    while True:
        try: choice = int(input('Choose a number beetween 0 and 36: '))
        except KeyboardInterrupt: return
        except: continue
        
        if choice not in range(0,37):
            print('Not a valid number')
            continue
        
        green = 0
        red = range(1,11,2) + range(12,19,2) + range(19,29,2) + range(30,37,2)
        black = [x for x in range(1,37) if x not in red]
        
        if choice == green: print('You got green')
        if choice in black: print('You got black')
        if choice in red:   print('You got red')
        
        try: play_again = raw_input('Pick again? (y/n): ') == 'y'
        except: return
        if not play_again: return
    
choose_color()
