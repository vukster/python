### Calculator ###

num1 = int(input("What is your first number?"))
num2 = int(input("What is your second number?"))
operation = input("Which basic arithemtic operation do you want to use? '+', '-', '*' or '/'")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else :
    print("you did not choose the right operator")