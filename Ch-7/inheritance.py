class Parent:
    def __init__(self):
        self.super_attribute=True
        print("This is super class..")

class child(Parent):
    def __init__(self):
        super().__init__()
        print("This is child class..")
    
# child1=child()
super1=Parent()      