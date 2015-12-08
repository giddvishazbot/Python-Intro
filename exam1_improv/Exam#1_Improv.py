def main():
    tax_info = auto_tax()
    tax_amount = tax_amount_calc(tax_info[1])
    
    print('Your vehicle code is %s' % tax_info[0])
    print('Your vehicle tax rate is {}%'.format(tax_info[1] * 100))
    print('your assessed ammount is %d' % tax_amount[0])
    print('Your assessed amount is {:,}'.format(tax_amount[0])) # https://docs.python.org/3/library/string.html#format-string-syntax
    print('your tax amount is %d' % tax_amount[1])

def tax_display():
    return


def auto_tax():
    car_tax_rate = {'m' : 0.03, 'c' : 0.05, 's' : 0.07, 't' : 0.08}
    print('motorcycle = m')
    print('Passenger car = c')
    print('Sports Utlity vehicle = s')
    print('Pick up truck = t')
    code = raw_input('Enter vehicle code: ')
    while code not in car_tax_rate.keys():
        print('need to use one of the codes')
        code = raw_input('Enter vehicle code: ')
    return code, car_tax_rate[code]


def tax_amount_calc(tax_rate): 
    assessed_ammount = int(input('Enter the value of your vehicle: '))
    
    tax_amount = tax_rate * assessed_ammount
    return assessed_ammount, tax_amount

main()
