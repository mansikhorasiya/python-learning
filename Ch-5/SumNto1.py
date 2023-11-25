def sum_N_to_1(n):
    # base case
    if n == 0:
        return 1
    # recursive case
    ans = n + sum_N_to_1(n-1)
    return ans
n = int(input("Enter the number :"))
print(sum_N_to_1(n))