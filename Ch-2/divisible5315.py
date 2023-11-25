num = int (input("Enter the number:"))

# checking  wheter it is divisible by 15
if num % 15 ==0:
    print("it is divisible by 15..")
else:
# chaecking wheter it is divisible by 3 or 5
    if num % 3 ==0 or num % 5 ==0:
        print("this num is not divisible by 15 bt divible by 3 or 5..")
    else:
        print("the num is divisible by 3 Nor 5..")