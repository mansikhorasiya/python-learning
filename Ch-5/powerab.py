def power_a_b(a,b):

    # base case
    if b == 0:
        return 1
    
    # recursive case
    ans =  a *power_a_b(a,b-1)
    return ans

a = int(input('Enter the numbe1:'))
b = int(input('Enter the numbe2:'))

print(power_a_b(a,b))