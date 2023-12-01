n=int(input("Enter no of students :"))
student_info={}
for i in range(n):
        print('Enter student info')
        Name=(input("Name: "))
        rollnumber=int(input("rollnumber: "))
        marks=int(input("marks: "))
        student_info['Name{}'.format(i)]=Name
        student_info['rollnumber{}'.format(i)]=rollnumber
        student_info['marks{}'.format(i)]=marks
        # student_info[i]={'Name':Name,'rollnumber':rollnumber,'marks':marks}
# print(student_info)
