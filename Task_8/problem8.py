
q = int(input())

for  n in range(0,q):
    lenght = int(input())
    numbers = list(map(int, input().split()))
    print(max(numbers)-min(numbers))
