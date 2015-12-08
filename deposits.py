def input_gather():
    
    name = input('Hello, what is the name of the customer you are processing today?')
    yesterday_balance = input(" and they're balance yesterday?")
    today_deposit = input(" and today's deposits")
    today_withdrawals = input(" and today's withdrawals?")
    
    processing(yesterday_balance, today_deposit, today_withdrawals)
    customer_output(name)
    
def another_customer():
    while True:
        try:
            another_customer = input('Do you have another customer to process?')
            if another_customer() not in ['y', 'n']:
                print("Please enter 'y' or 'n'")
                continue
            return another_customer() == 'y'
        except KeyboardInterrupt:
            raise
        except:
            raise
return

def processing( yesterday_balance, today_deposit, today_withdrawals):
    
    yesterday_balance + today_deposit - today_withdrawals = new_balance
    customer_output(new_balance)
    
    
def customer_output(name, new_balance):
    customer_balance = new_balance
    if customer_balance <= 0:
        print('{}, {}:   ***** Account Overdrawn *****'.format(name, customer_balance) # you're missing a ) for the print()
    else:
        print('{}, {}:'.format(name, customer_balance)
        
    another_customer()