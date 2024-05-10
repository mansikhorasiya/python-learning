# num=int(input('Enter any number:'))
# sum=0
# temp=num

# while temp>0:
#     digit = temp % 10
#     cube = digit ** 3
#     sum = sum+cube
#     temp //= 10
# if sum == num:
#     print('it is an Armstrong Number')
# else:
#     print('it is not an Armstrong Number')
# >>>>>>>>>>>>>>>>>>>>>>>>

class ArmstrongChecker:
    def __init__(self, num):
        self.num = num
    
    def check_armstrong(self):
        sum_of_cubes = 0
        temp = self.num

        while temp > 0:
            digit = temp % 10
            cube = digit ** 3
            sum_of_cubes += cube
            temp //= 10

        if sum_of_cubes == self.num:
            return True
        else:
            return False

# Input number from the user
num = int(input('Enter any number: '))

# Create an instance of ArmstrongChecker
armstrong_checker = ArmstrongChecker(num)

# Check if the number is an Armstrong number
if armstrong_checker.check_armstrong():
    print('It is an Armstrong Number')
else:
    print('It is not an Armstrong Number')
