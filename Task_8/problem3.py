
q = int(input())

for i in range(0,q):
    word = input()
    lenght = len(word)

    if lenght > 10:
        print(f"{word[0]}{lenght-2}{word[lenght-1]}")
    else:
        print(str(word))