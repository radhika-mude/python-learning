hrs = int(input(" Enter the number of hour: "))
rate = float(input(" Enter the rate: "))

def compute_pay() :
    if hrs > 50:
        pay = ( hrs * rate) + (( hrs - 50 ) * rate * 1.5)
    else:
        pay = hrs * rate
    return pay

pays = compute_pay()
print("Pay: ", pays)