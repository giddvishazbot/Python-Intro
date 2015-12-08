def main():
    palindrome()
    more_test()

def palindrome():
        my_str = input("Enter a string: ")
        my_str = my_str.casefold()
        rev_str = reversed(my_str)
        if list(my_str) == list(rev_str):
            print("It is palindrome")
        else:
            print("It is not palindrome")
def more_test():
    while True:
        try:
            more_test = input('Want to try another palindrome? (y/n) ').lower()
            if more_test not in ['y', 'n']:
                print("Please enter 'y' or 'n'")
                continue
            if more_test == 'y':
                palindrome()
            else:
                break
        except KeyboardInterrupt:
            raise
        except:
            raise
main()

