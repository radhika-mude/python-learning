numlist = list()
while True:
    x = input('ENTER A NUMBER: ')
    if x == 'done':
        break

    x = float(x)
    numlist.append(x)

if len(numlist) > 0:
    avg = sum(numlist) / len(numlist)
    print('Average:', avg)
else:
    print('No numbers entered.')

