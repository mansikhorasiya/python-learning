# writting a function  for caluculate 1 to n
def sumoneton(n):
    sum=0
    for i in range(1 ,n+1):
        sum +=i
    return sum

n=int(input("Enter n:"))
# call the function'
outpu1=sumoneton(n)
print("sum of all numbers  till  n is:",outpu1)
