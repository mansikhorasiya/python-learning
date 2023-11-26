class vehical():
    def __init__(self,seating_capicity):
        self.seating_capicity = seating_capicity
    def Get_fare(self):
        return self.seating_capicity * 100
    
class bus(vehical):
    def __init__(self, seating_capicity):
        super().__init__(seating_capicity)
    def Get_fare(self):
        vehical_fare=super().Get_fare()
        maintanace_fare=0.1 * vehical_fare
        total_fare=vehical_fare + maintanace_fare
        return total_fare
vehical1= vehical(50)
print("This is vahecale fare",vehical1.Get_fare())

bus1= bus(50)
print("this is bus fare",bus1.Get_fare())
        