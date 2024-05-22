# n=int(input("enter no of row:"))
# for i in range(n):
#     print(' ', *(n-i),"*" *(2*n+1))
# for m in range(n-2,-1,-1):
#     print(' ' *(n-m),"*" *(2*n+1))

n = int(input("please enter diamond's height:"))

# for i in range(n):
#     print(" "*(n-i), "*"*(i*2+1))
# for i in range(n-2, -1, -1):
#     print(" "*(n-i), "*"*(i*2+1))

for i in range(n):
    print(" "*(n-i),"*"*(i*2+1))
for i in range(n-2,-1,-1):
    print(" "*(n-i),"*"*(i*2+1))