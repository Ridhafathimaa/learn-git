#python calculator:

num1 = float(input("enter your first number: "))
num2 = float(input("enter your second number: "))
operator = input("select one operator (+,-,*,/): ")
if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("invalid operator")