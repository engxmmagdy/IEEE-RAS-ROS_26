
q = int(input())

for i in range(0,q):
    numbers = list(map(int, input().split()))
    
    if numbers[0]+numbers[1] == numbers[2] or numbers[0]+numbers[2] == numbers[1] or numbers[1]+numbers[2] == numbers[0]:
        print("YES")
    else:
        print("NO")