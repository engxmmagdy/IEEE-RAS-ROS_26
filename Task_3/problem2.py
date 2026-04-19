#______________moving in 2D_______________

def move_player(x,y,x_direction,y_direction):
    if x_direction == "r":
        x += 1
    elif x_direction == "l":
        x -= 1
    if y_direction == "u":
        y += 1
    elif y_direction == "d":
        y -= 1
    return x , y


x = int(input("X_coordinate: "))
y = int(input("Y_coordinate: "))
x_direction = input("l/r/n for(LEFT/RIGHT/NON): ")
y_direction = input("u/p/n for(UP/DOWN/NON): ")

print("New coordinates: "+format(move_player(x, y, x_direction, y_direction)))