
n = int(input())

for i in range(0,n):
    
    l = int(input())
    numbers = input().split()

    if numbers[0] == numbers[1]:
        repeated = numbers[0]
    elif numbers[0] == numbers[2]:
        repeated = numbers[0]
    else:
        repeated = numbers[1]
    
    x = 0
    for k in numbers:
        x += 1
        if k != repeated:
            print(x)
