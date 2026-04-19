#_________________calculate bill_____________

menu = {"apple":0.5 , "orange":0.4, "fury":0.6, "cheese":0.8}


def calculate_bill(menu, bill):
    sum = 0
    for i in bill:
        x = menu[i]
        sum += x
    return "Total bill: L.E "+format(sum)


bill = input("Enter products: ").split()
print(calculate_bill(menu, bill))