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
         
lst1 = ['W', 'a', 'w', 'b']
lst2 = ['e', ' ', 'riting', 'log']
lst3 = [x + y for x, y in zip(lst1, lst2)]
print(lst3)












