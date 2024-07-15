# Q1. Convert a given string to int using a single line of code.
# a = '5'
# print(int(a))

# Q2. Write a code snippet to convert a string to a list.
# str = "Analytics Vidhya"
# print(str.split(" "))

# Q3. Write a code snippet to reverse a string.
# str  = "Analytics Vidhya"
# str1 = " "
# for i in str:
#     str1 = i + str1
# print("the orignal string:", str)
# print("the reversed string: ", str1)

# Q4. Write a code snippet to sort a list in Python.
# numbers = [5, 8, 9, 1]
# numbers.sort()
# print(numbers)

# Q6. How can you delete a file in Python?
# import os
# os.remove("txt1.txt")

# Q8. different ways of deleting an element from a list.
# There are two ways in which we can delete elements from the list:

# 1. By using the remove() function
# list1 = [5, 4, 2, 8]
# list1.remove(2)
# print(list1)

# 2. By using the pop() function
# list1 = [1 ,2 ,3]
# list1.pop(1)
# print(list1)

# Q9. Write a code snippet to delete an entire list.
# list1 = [1 ,2 ,3, 4]
# list1.clear()
# print(list1)

# Q10. Write a code snippet to reverse an array.
# The two ways of reversing an array are as follows:

# 1. Using the flip() function
# import numpy as np
# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.flip(arr1)
# print(arr2)

# 2. Without using any function

# import numpy as np
# arr1 = np.array([1, 2, 3, 4])
# arr2 = arr1[::-1]
# print(arr2)

# Q11. Write a code snippet to get an element, delete an element, and update an element in an array.
# import numpy as np
# arr2 = [1, 2, 3, 4]
# x = np.delete(arr2, 0)
# print(x)

# Q12. Write a code snippet to concatenate lists.
# List1= [“W”, “a”, “w”,”b”]
# List2 = [“e”, “ “,”riting”,”log”]
         
# lst1 = ['W', 'a', 'w', 'b']
# lst2 = ['e', ' ', 'riting', 'log']
# lst3 = [x + y for x, y in zip(lst1, lst2)]
# print(lst3)

# Q13. Write a code snippet to generate the square of every element of a list.
# my_list = [2 ,3 ,4 ,5]
# list_finl = []
# for i in my_list:
#     list_finl.append(i * i)
# print(list_finl)

# Q21. What is the difference between split and join?
# Split and join are both functions of Python strings,
# but they are completely different when it comes to functioning.
# a = 'this is string'
# b = a.split(' ')
# print(b)  # ['this', 'is', 'string']

# c = ' '.join(b)
# print(c)  # 'this is string'


# Q23. Explain the top 5 functions used for Python strings.

# len(): this  function returns the  lenght of a  string
# s = "hello mansi"
# print(len(s))
# strip(): This function removes leading and trailing whitespace from a string.
# s = "hello mansi"
# print(s.strip())
# replace(): This function replaces all occurrences of a specified string with another string.
# s = 'Hello, Mansi!'
# print(s.replace('Mansi', 'Universe'))
# split(): This function splits a string into a list of substrings based on a delimiter.
# s = 'Hello, World!'
# print(s.split(','))
# upper() and lower(): These functions convert a string to uppercase or lowercase, respectively.
# s = 'Hello, World!'
# print(s.upper())
# print(s.lower())

# Q32. What are global and local variables in Python?
# This is a global variable
# x = 10
# def func():
#     # This is a local variable
#     x = 5
#     print(x)
# func()
# print(x)

# Q51. Write a program to check whether a number is prime or not.
# from math import sqrt

# def prime_or_not(number):
#     for i in range(2, int(sqrt(number)) + 1):
#         if number % i == 0:
#             return 0
#     return 1

# Q53. What are the ways to swap the values of two elements?

# a = 'this is string'
# b = a.split(' ')
# print("Before swap:")
# print("a =", a)  # 'this is string'
# print("b =", b)  # ['this', 'is', 'string']

# # Swapping values
# temp = a
# a = b
# b = temp

# print("After swap:")
# print("a =", a)  # ['this', 'is', 'string']
# print("b =", b)  # 'this is string'

# Q54. Write a program in Python to return the factorial of a given number using recursion.
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Test the function
number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")










