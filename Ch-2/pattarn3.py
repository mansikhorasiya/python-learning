# n = int(input("Enter n:"))
# for i in range(1,n+1):   #Loops for row
#     for j in range(1,i+1):#Loops for column
#         print(j,end="")
#     print()
 
# outer loop
for i in range (65,70):
    # inner loop
    for j in range(65,i+1):
        print(chr(j),end="")
    print()