class Student:
    def set_name(self,name):
        self.name=name

    def get_name(self):
        return self.name
    
Student1=Student()
Student1.set_name("mansi")
print(Student1.name())