input1 = int(input("Select a number between 1 and 100"))

for x in range(0, input1):
    check_count = x+1

    buzz = False
    fizz = False

    if ((check_count % 3) == 0) and ((check_count % 5) == 0):
        print("fizzbuzz")
    elif (check_count % 3) == 0:
        print("fizz")
    elif (check_count % 5) == 0:
        print("buzz")
    else:
        print(check_count)




