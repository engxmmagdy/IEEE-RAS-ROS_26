nums = []

while True:
    n = int(input("Enter number (-1 to stop): "))
    
    if n == -1:
        break
    
    nums.append(n)

print("Max:", max(nums))
print("Min:", min(nums))