#write a function that prints hello world!
# def printHello():

#     # body of function
#     print("Hello world!")

# printHello()

# def add(n1=0,n2=0):
#     print("n1:",n1)
#     print("n2:",n2)
#     sum=n1+n2
#     return sum

#positinal argument
# print("the sum is",add(3,2))

#keyword argument 
#print("the sum is",add(n1=3,n2=2))

# default argument
# print("the sum is", add(3))

# variable lenght argument
# def addAllNumber(*args):
#      sum=0
#      for i in args:
#           sum +=i
#      return sum
# output = addAllNumber(2,3,4,5,6,7,8,9)
# print("The sum is:", output)

#keyword argument(**kwa)
def studentInfo(**kwas):
    for x,y in kwas.items():
        print(x,"is",y)

studentInfo(name="urvi", age=22, city="delhi")
studentInfo(name="mansi",age=21,city="bagsra")

 
