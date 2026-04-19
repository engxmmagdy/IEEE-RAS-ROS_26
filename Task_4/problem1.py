

def safe_divide():
    try:
        x = int(input("First number: "))
        y = int(input("Second number: "))
        return x/y
    except ZeroDivisionError:
        return "cannot divide by zerp"
    except ValueError:
        return "only numbers"

print(safe_divide())