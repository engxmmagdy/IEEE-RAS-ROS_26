#______________-picking random winner______________

'''
import random

def pick_winner(names):
    if len(names) == 0 :
        print("List is empty")
    else:
        print("Congratulations "+random.choice(names))


names = input("Enter competitors names: ").split()
pick_winner(names)
'''

# using ___RETURN___
import random

def pick_winner(names):
    if len(names) == 0 :
        return "List is empty"
    else:
        return "Congratulations "+random.choice(names)


names = input("Enter competitors names: ").split()
print(pick_winner(names))
