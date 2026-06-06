# Simple Calculator for the Bro Code YT tutorial
print("====================================================================")
print("====================Simple Calculator v1.0==========================")
print("====================================================================")

# Functions (Addition, Subtraction, division and multiplication.)
def addition(x, y):
    return x + y

def subtraction(x, y):
    return x-y

def division(x, y):
    if y == 0:
        return "Error: Division by 0 not possible"
    else:
        return x / y
    
def multiplication(x, y):
    return x * y

# Request User Input
act = input("What would you like to do? (+, -, *, /): ")
x = float(input("Please input your first number: "))
y = float(input("Please input your second number: "))

# Calculate and print result
if act == "+":
    res = addition(x, y)
elif act == "-":
    res = subtraction(x, y)
elif act == "*":
    res = multiplication(x, y)
elif act == "/":
    res = division(x, y)
else:
    print("An Error occured please try again.")

print("====================================================================")
print(x, act, y, " = ", res)
print("====================================================================")
