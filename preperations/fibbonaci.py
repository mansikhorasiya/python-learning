# num = int(input("Enter any number:"))
# n1 , n2 = 0 , 1
# sum = 0
# if num <= 0:
#     print("please enter number greater than 0")
# else:
#     for i in range(0, num):
#         print(sum , end=" ")
#         n1 = n2
#         n2 = sum
#         sum = n1 + n2
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>.
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# # Example usage:
# fn1= fibonacci()
# for i in range(10):
#     print(next(fn1))

num=int(input("Enter any number:"))
def fibbonacci():
    a , b = 0,1
    while True:
        yield a 
        a , b= b, a+b
fn1=fibbonacci()
for i in range(0 , num):
    print(next(fn1))