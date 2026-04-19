#_______________analyzing grades_____________

grades = input("Grades: ").split()

def analyze_grades(grades):
    
    min = None
    max = None
    sum = 0
    students = 0

    for i in grades:
        x = int(i)
        if min == None or x < min:
            min = x
        if max == None or x > max:
            max = x
        sum += x
        students += 1
    avr = sum/students
    return "maximum: "+format(max)+"\n"+"minimum: "+format(min)+"\n"+"average: "+format(avr)

print(analyze_grades(grades))

    

