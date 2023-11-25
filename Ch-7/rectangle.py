n=int(input("Enter the hight:"))
n1=int(input("Enter the width:"))
class Rectangle:
    def set_dimenstion(self,height,widht):
        self.height = height
        self.width = widht
    
    def area(self):
         return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.width)
# creating object 
object1= Rectangle()
object1.set_dimenstion(n,n1)
print("this height and width ",object1.height,object1.width)
print("this is area",object1.area())
print("this is perimeter",object1.perimeter())