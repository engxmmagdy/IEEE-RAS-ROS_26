#________________six random numbers from 1 to 50_________________

import random


def get_unique_lottery():

    #filling the range
    x = set()
    n = 1
    while True:
        x.add(n)
        n +=1
        if n == 51:
            break


    #doing the function
    six_elements = set()
    while True:
        num = random.choice(list(x))
        six_elements.add(num)
        if len(six_elements) == 6:
            break

    return "six random numbers: "+format(six_elements)

print(get_unique_lottery())

    
    