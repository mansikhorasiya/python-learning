k=0
n=int(input("Enter num of row:"))
for m in range(n, 0, -1):
    k +=1
    for j in range(1,m + 1):
        print(k, end=' ')
    print()
