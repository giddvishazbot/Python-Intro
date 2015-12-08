def main():
    print('Your tax amount is ${:,}'.format(tax_amount_calc()))


def auto_tax():
    car_tax_rate = {'m' : 0.03, 'c' : 0.05, 's' : 0.07, 't' : 0.08}
    print('motorcycle = m')
    print('Passenger car = c')
    print('Sports Utlity vehicle = s')
    print('Pick up truck = t')
    code = input('Enter vehicle code: ')
    while code not in car_tax_rate.keys():
        print('Need to use one of the codes')
        code = input('Enter vehicle code: ')
    return car_tax_rate[code]


def tax_amount_calc(): 
    tax_rate = auto_tax()
    while True:
        try:
            assessed_ammount = int(input('Enter the value of your vehicle: '))
            if assessed_ammount < 0:
                raise ValueError()
            break
        except:
            print('Please enter a valid non-negative integer vehicle value')
    
    tax_amount = tax_rate * assessed_ammount
    return tax_amount


main()
