#____________________common elements in two sets________________

first = set(input("first set: "))
second = set(input("second set: "))

#first = {1,2,3,4}
#second = {3,4,5,6}

def common(first,second):
    result = set()
    for x in first:
        if x in second:
            result.add(x)
    return "Common numbers: "+format(result)

print(common(first,second))