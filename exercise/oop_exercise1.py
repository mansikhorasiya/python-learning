# create a class  with instance attribute:

# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

a = int(input("Enter max_speed : "))
b = int(input("Enter mileage: "))

# modelx = Vehicle(240,18)
modelx = Vehicle(a,b)

print(modelx.max_speed,modelx.mileage)

