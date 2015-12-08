green = 0
red = range(1, 11, 2) + range(12, 19, 2) + range(19, 29, 2) + range(30, 37, 2)
# [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
black = [x for x in range(1, 37) if x not in red]

choice = input('Choose a number beetween 0 and 36: ')

if choice == green:
    print('You got green')

if choice in black:
    print('You got black')

if choice in red:
    print('You got red')
    
if not choice >= 0 or not choice <= 36:
    print('Please enter a valid number')
