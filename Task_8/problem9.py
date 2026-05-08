
q = int(input())
available_rooms = 0

for n in range(0,q):
    data = list(map(int, input().split()))
    if data[1]-data[0] >= 2:
        available_rooms += 1

print(available_rooms)