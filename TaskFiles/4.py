# # Example list of random numbers
numbers = [5, 8, 2, 1, 6, 5, 7, 6]

# def find_second_largest(numbers):
#     # Find the maximum number
#     max_number = max(numbers)
#     # Remove the maximum number from the list
#     numbers.remove(max_number)
#     # Find the maximum number again (now it will be the second largest)
#     second_largest = max(numbers)
#     return second_largest


# # Find the second largest number
# second_largest = find_second_largest(numbers)
# print("The second largest number is:", second_largest)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class SecondLargestFinder:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def find_second_largest(self):
        # Remove duplicates and sort the list
        sorted_numbers = sorted(set(self.numbers))
        
        # Check if there are at least two unique numbers in the list
        if len(sorted_numbers) < 2:
            return "There is no second largest number."
        else:
            return sorted_numbers[-2]

# Create an instance of SecondLargestFinder
finder = SecondLargestFinder(numbers)

# Find the second largest number
second_largest = finder.find_second_largest()
print("The second largest number is:", second_largest)

