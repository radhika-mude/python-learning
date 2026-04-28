largest = None
count = 0

while True:
    num = (input("Enter a number( type done to finish ): "))

    if num == "done":
        break

    num = float(num)
    if largest is None or num > largest:
        largest = num
    count = count + 1
print(" Largest number", largest)
