x = input(" ENTER A NUMBER: ")
try :
    x = int(x)
except :
    print(" please enter a valid number")
    quit()
if x > 0 :
    print(" num is greater than zero ")
elif x == 0 :
    print(" num is 0 ")
else :
    print(" num is less than zero ")
print(" yayyy ")