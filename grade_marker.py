try:
    grade = float(input(" ENTER YOUR GRADE "))
    if 1.0 > grade >= 0.9:
        print(" A ")
    elif 0.9 > grade >= 0.8:
        print(" B ")
    elif 0.8 > grade >= 0.7:
        print(" C ")
    elif 0.7 > grade >= 0.6:
        print(" D ")
    elif 0.0 < grade < 0.6:
        print(" F ")
    else:
        print("Grade must be between 0.0 and 1.0")
except:
    print(" INSERT A VALID GRADE BETWEEN 0.1 TO 1.0 ")
