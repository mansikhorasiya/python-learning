# create a child class Bus that  will inherit all of the variables and methods of  the vehicle class
class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(vehicle):
    pass

school_Bus = Bus("school volvo",180,12)
print("vehicle name:",school_Bus.name ,"speed:",school_Bus.max_speed ,"mileage:",school_Bus.mileage)
        