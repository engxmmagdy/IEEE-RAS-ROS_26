
q = int(input())
passengers = 0
max_passengers = 0

for i in range(0,q):
    data = list(map(int, input().split()))
    out = data[0]
    enter = data[1]
    passengers = passengers - out + enter
    if passengers > max_passengers:
        max_passengers = passengers

print(max_passengers)

