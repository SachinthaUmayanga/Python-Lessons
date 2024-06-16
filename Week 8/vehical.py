class Vehicle:
    
    def speed(self):
        print("Vehicle can spped")
        
    def breaking(self):
        print("Vehicles can break")
        
class Jeep(Vehicle):
    
    def four_weel_drive(self):
        print("Jeep have four weel drive")
        
jeep = Jeep()

jeep.speed()
jeep.breaking()

jeep.four_weel_drive()