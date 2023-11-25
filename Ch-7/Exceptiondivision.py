A= int(input("Ennter number1:"))
B= int(input("Enter number2:"))

try:
    result= A / B
except ZeroDivisionError:
    result=None
    print("Error: Cannot divide by zero..")
finally:
    print("complete division opration:",result)