def opening_display():
    try:
        file_use = input('Welcome, would you like to create your phonebook, add to it, or read from it?')
        print('Enter "Create" to make a new phonebook')
        print('Enter "Add" to add to the current phonebook')
        print('Enter "Read" to look up a friend')
        if file_use not in ['Read', 'Add', 'Create']:
            print('Enter a valid input please')
            continue # what loop?
        return file_use
    except KeyboardInterrupt:
        raise
    except:
        print('Not valid input') # then end?
    
def create_book():
    import os.path
    try:
        phone_book = open('phonebook.txt' , 'w')
        if os.path.exists(phone_book): 
            break # break what?
        else:
            phone_book.close()
            #reopen display?
    finally: # means, "after whatever happens with the try-raise, do this stuff"
        return

        

def name_to_book():
#Dictionary for both values and one function would be better
    while True:
        try:    
            phone_book =open('phonebook.txt' , 'a')
            name =input('Enter the name of your friend')
        except KeyboardInterrupt:
            raise
        else:
            phone_book.write(name + '/n')
            #merge with phone_to_book

# this looks really familiar... seems a lot like name_to_book
# maybe you could make one function and have it work for both somehow?
def phone_to_book():
    while True:
        try:
            phone_book =open('phonebook.txt' , 'a')
            phone_number =input('And their phone number too')
        except KeyboardInterrupt:
            raise
        else: # try-else isn't a thing, do you mean try-except?
            phone_book.write(Phone_number + '/n')
        #merge with name_to_book
        return
    
def add_again():
    while True:
        try:
            addmore =input("Would you like to continue? ('y' or 'n') ")
            if addmore not in ['y', 'n']:
                print("Enter 'y' for yes or 'n' for no please'")
                continue
            return addmore == 'y'
        except KeyboardInterrupt:
            raise
        else: # try-else isn't a thing, do you mean try-except?
            break
    return False
    phone_book.close() # doesn't exist in this scope

def read_book():
    phone_book =open('phonebook.txt' , 'r')
    while True:
        try:
            name = input('What is the name of your friend your searching for?')
            if name not = # wut
            print('Im sorry but your friend seems to not be listed, perhaps your spelling is off?')
        except KeyboardInterrupt
            raise
        print(" Your friend {}'s number is {}.")
        read_more=input("Search for another friend? 'y' for yes or 'n' for no")
        if read_more == 'y'
            return True:
    phone_book.close()
    
def name_phone_to_book(): # wut
    #for the love of god i hate everything
    person_phone_list{'': ,}
    input('Enter the name of your friend
