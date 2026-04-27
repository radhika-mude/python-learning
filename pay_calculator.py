hrs = int(input(' Enter the number of hours : '))
rate = float(input(' Enter the rate per hour : '))

if hrs > 40 :
    pay = (40 * rate) + ((hrs - 40) * rate * 1.5)
else:
    pay = hrs * rate

print("TOTAL PAY = ", pay)