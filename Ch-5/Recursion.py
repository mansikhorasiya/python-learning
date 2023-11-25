def factorial(n):
    #  base class
    if n == 0:
        return 1
    # recursive  case
    ans = n * factorial(n-1)
    return ans
n = int(input("Enter the number:"))
print(factorial(n))
    
