# define a property that must have the  same  value for  every class instance(object)
#   Define  a class attribute "color" with  a default value white..

class vehicle:
    #class attribute
    color = "white"

    def __init__(self, name , max_speed , mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(vehicle):
    pass
class Car(vehicle):
    pass

school_bus = Bus("school volvo",180,12)
print("color:",school_bus.color,school_bus.name,"speed:",school_bus.max_speed,"mileage:",school_bus.mileage)

Car = Car("Audi Q5",240,18)
print("color:",Car.color,Car.name,"speed:",Car.max_speed,"mileage:",Car.mileage)
print()