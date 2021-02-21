print("The program greets user and describes what's the purpose of the program.")
onemoretime = True

while onemoretime == True:
    input1 = int(input("Enter number of km"))
    print(input1*1.609)

    ques1= input("Do you want another conversion?")
    ques2 = "NOK"

    while ques2 == "NOK":

        if ques1 == "No":
            onemoretime = False
            print ("Tank you for conversion")
            ques2 = "OK"

        elif ques1 == "Yes":
            onemoretime = True
            ques2 = "OK"

        else:
            ques2 = "NOK"

