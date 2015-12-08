def display(sorted_list):
    a = sum(sorted_list)
    print(' The max of the list is :', max(sorted_list))
    print(' The min of the list is :', min(sorted_list))
    print(' The sum of the numbers of the list is: {}' .format(a))
    print(' Lastly the average of the list is :', (sum(sorted_list) / len(sorted_list)))

def number_collection():
    number_list = []
    for i in range(19): 
        number = int(input('Enter a number'))
        number_list.append(number)
    display(number_list)
number_collection()
    

    

    

    
