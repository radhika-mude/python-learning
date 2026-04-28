smallest = None
count = 0

while True:
    num = (input("Enter a number( type done to finish ): "))

    if num == "done":
        break

    num = float(num)
    if smallest is None or num < smallest :
        smallest = num
    count = count + 1
print(" Smallest number: ", smallest)
print('Total numbers: ', count)
