# Simple Calculator
num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))
c = input("What operation do you want to do?( % / * / - / + ) : ")
if c == "%":
    print(num1 / num2)
elif c == "*":
    print(num1 * num2)
elif c == "+":
    print(num1 + num2)
elif c == "-":
    print(num1 - num2)
else:
    print("Give a valid input")
    exit()
