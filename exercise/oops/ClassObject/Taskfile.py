class student_info:
    def __init__(self,rollno,name):
        self.rollnumber=rollno
        self.name=name
class student_marks:
    def __init__(self,rollno,marks_one,marks_two,marks_three):
        self.rollno=rollno
        self.marks_one=marks_one
        self.marks_two=marks_two
        self.marks_three=marks_three
class Mainclass:
    def __init__(self):
        self.students=[]
        def input_students(self):
            s=int(input("Enter the number of student:"))
            for i in range(s):
                rollno=int(input("Enter student rollno:"))
                name=input("Enter student name:")
                marks_one=int(input("Enter mark for sub one:"))
                marks_two=int(input("Enter marks for sub two:"))
                marks_three=int(input("Enter marks for sub three:"))

                student_info = student_info(rollno, name)
                student_marks =student_marks(rollno, marks_one, marks_two, marks_three)

                self.students.append((student_info, student_marks))
def __average(self):
        __average(self.students_marks_one+self.students_marks_two+self.students_marks_three)
        return  __average


def calculate_average(self, marks_list):
     total_marks = sum(marks_list)
     return total_marks / len(marks_list)

def calculate_grade(self, average):
         if average >= 90:
             return "A"
         elif average >= 80:
            return "B"
         elif average >= 70:
            return "C"
         elif average >= 60:
            return "D"
         else:
            return "F"

def main(self):
        self.input_student_data()

        for student_info, student_marks in self.students:
            average_marks = self.calculate_average([student_marks.student_marks_one,
                                                    student_marks.student_marks_two,
                                                   student_marks.student_marks_three])

            grade = self.calculate_grade(average_marks)

            print("Student: {student_info.student_name} (Roll No: {student_info.student_rollno})")
            print("Average Marks: {average_marks:.2f}")
            print("Grade: {grade}")
            print("")

if __name__ == '__main__':
    main_instance=Mainclass()



