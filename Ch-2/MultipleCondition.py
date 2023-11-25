eng_marks =int(input("Enter the english marks : "))
math_marks =int(input("Enter the math marks : "))

# if both are more than 80,print A grade
if eng_marks > 80 and math_marks >80:
    print("A Grade..")

# if either of marks are more than 80 ,print B grade 
elif eng_marks >80 or math_marks >80:
    print("B Grade..")

# if neither of marks are more than 80 ,print C grade
else:
    print("C grade..")