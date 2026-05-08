
q = int(input())
teams = 0

for i in range(0,q):
    permissions = list(map(int, input().split()))
    x = 0
    
    for n in permissions:
        if n == 1:
            x += 1
    
    if x >= 2:
        teams += 1

print(teams)
