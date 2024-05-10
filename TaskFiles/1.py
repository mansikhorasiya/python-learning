class StudentInfo:
    def __init__(self,name):
        self.student_name = name


class StudentMarks:
    def __init__(self,marks1,marks2,marks3):
        self.subject_marks1 = marks1
        self.subject_marks2 = marks2
        self.subject_marks3 = marks3

    def calculate_average(self):
        total_marks = self.subject_marks1 + self.subject_marks2 + self.subject_marks3
        average_marks = total_marks / 3
        return average_marks

    
class Main:
    def __init__(self):
        self.students = []
        self.highest_average_marks = 0

    
    def input_students(self):
        num_students=int(input('Enter the number of students:'))

        for i in range(num_students):
            student_name = input('Enter student name:')
            student_info = StudentInfo(student_name)
            self.students.append(student_info)
        
    def input_marks(self):

        for student in self.students:
            student_name = student.student_name
            marks1 = int(input(f"Enter student {student_name} marks for subject 1: "))
            marks2 = int(input(f"Enter student {student_name} marks for subject 2: "))
            marks3 = int(input(f"Enter student{student_name} marks for subject 3: "))
            student_marks = StudentMarks(marks1, marks2, marks3)
            student.student_marks = student_marks

    def calculate_grade(self):
        for student in self.students:
            average_marks = student.student_marks.calculate_average()
            if average_marks >= 90:
                grade = "A"
            elif average_marks >= 80:
                grade = "B"
            elif average_marks >= 70:
                grade = "C"
            elif average_marks >= 60:
                grade = "D"
            else:
                grade = "F"
            student.grade = grade
            #  topper information if necessary
            if average_marks > self.highest_average_marks:
                self.highest_average_marks = average_marks
                self.topper = student



    def print_student_info(self):
        for student in self.students:
            print(f"Student Name: {student.student_name}")
            print(f"Average Marks: {student.student_marks.calculate_average()}") 
            print(f"Grade: {student.grade}")
            print(f"Topper: {self.topper.student_name} with an average of {self.highest_average_marks} marks.")

            print()


    def run(self):
        self.input_students()
        print()
        self.input_marks()
        print()
        self.calculate_grade()
        print()
        self.print_student_info()

        

main = Main()
main.run()





        




    
