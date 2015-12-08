def get_string_input(prompt):
    while True:
        try:
            name = input(prompt)
            if not len(name) > 0:
                raise ValueError
            return name
        except KeyboardInterrupt:
            raise
        except:
            print('Invalid input, please try again.')


def get_csv_output_path():
    from datetime import datetime as dt
    import os
    
    csv_file = get_string_input('Enter the output filepath: ')
    if not os.path.isfile(csv_file):
        ts = dt.today().strftime('%Y%m%d%H%M%S')
        return os.path.join(os.getcwd(), ts + '_customers.csv')
    

def get_numeric_input_for_customer(prompt, customer, is_valid_func):
    while True:
        try:
            num = float(input(prompt))
            print(num)
            if not is_valid_func(num, customer):
                continue
            return num
        except KeyboardInterrupt:
            raise
        except:
            print('Invlaid input, please try again.')

csv_output_path = get_csv_output_path()

customer_name = get_string_input('Enter the Customer Name: ')
balance = 0
deposits = 0
withdrawals = 0
