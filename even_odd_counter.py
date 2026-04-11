even_count = 0
odd_count = 0

while True:
    num = input("type a number print done if you wanna stop")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("invalid input")
        continue
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("even:", even_count)
print("odd:", odd_count)




    


