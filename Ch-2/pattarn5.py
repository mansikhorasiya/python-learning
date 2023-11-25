n = int(input("Enter n:"))
for i in range(1, n+1): #loops for row
    # printing space
    print(" " * (n-i), end="")
    # printing digit
    for j in range(1, 2 * i):
        print(j, end="")
    print()