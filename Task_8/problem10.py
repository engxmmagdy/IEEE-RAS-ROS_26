
x = input()
n = []
i = 0

while i < len(x):
    if x[i] == ".":
        n.append("0")
    elif x[i] == "-":
        if x[i+1] == ".":
            n.append("1")
        elif x[i+1] == "-":
            n.append("2")
        i += 1
    i += 1

output = ''.join(n)
print(output)
