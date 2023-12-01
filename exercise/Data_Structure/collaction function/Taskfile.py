n= int(input("Enter no of students :"))
student_info={}
for i in range(n): 
    print('Enter student info:')
    rollnumber = int(input("rollnumber: "))
    name=(input("name: "))
    marks=int(input("marks: "))
    student_info[i]={'Name':name,'rollnumber':rollnumber,'marks':marks,'grade':None}

for a,b in student_info.items():
    for c,d in (b.items()):
        if c == "marks":
            if (d >= 90 and d <= 100):
                b["grade"] = "A"
            elif (d>=80 and d<=90):
                 b["grade"] = 'B'
            elif (d>=60 and d<=80):
                 b["grade"] = 'C'
            elif (d>=40 and d<=60):
                 b["grade"] = 'D'
            elif (d<=40):
                 b["grade"]='fail'
            else:
                print()

print(student_info)

