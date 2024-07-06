# def sum_to_single_digit(lst):
#     total_sum = sum(lst)
    
#     while total_sum > 10:
#         total_sum = sum(int(digit) for digit in str(total_sum))
    
#     return total_sum


# digits = [1, 2, 3, 4, 5]
# result = sum_to_single_digit(digits)
# print(result)


# def reduce_to_single_digit(n):
#     while n >= 10:
#         temp_sum = 0
#         while n > 0:
#             temp_sum += n % 10
#             n //= 10
#         n = temp_sum
#     return n

# input_str = input("Enter digits separated by space: ")
# print(input_str)
# digits = list(map(int, input_str.split()))
# print(digits)

# total_sum = 0
# for digit in digits:
#     total_sum += digit
# print(total_sum)

# single_digit_result = reduce_to_single_digit(total_sum)

# print("The single digit sum is:", single_digit_result)

n = input("Enter any number:")

for i in range(len(n)):
    n=str(sum(int(digit) for digit in n))
    if len(n) == 1:
        break;
        
print(n)
