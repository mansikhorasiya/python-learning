n= (input("Enter any string:"))

def is_pallindrome(s):
    return s == s[::-1]
    

if is_pallindrome(n):
    print("The string is a palindrome")
else:
    print("The string is  not palindrome")
