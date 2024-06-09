class vehicle:
    def __init__(self,_tyres, _headlight, _seats) -> None:
        self.tyres = _tyres
        self.headlight = _headlight
        self.seats = _seats
        
    def drive_mode(self):
        return "mode"
    
    def speed(self):
        return "speed"
    
    def condition(self):
        return "condition"
    
    def upgrade(self):
        return self.headlight + " " +self.tyres+ " " +self.seats
    
vehicle = vehicle("big", "dsi", "recaro")
print(vehicle.upgrade())