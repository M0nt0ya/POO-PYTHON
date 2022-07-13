from car import Car

class UberConfort(Car):
    numberPassager    = int
    carAccepted       = []
    seatMaterial      = []
    
    """ Constructor de herencia"""
    def __init__(self, license, driver, carAccepted, seatMaterial, numberPassager):
        super.__init__(license, driver)
        self.carAccepted     = carAccepted
        self.seatMaterial    = seatMaterial
        self.numberPassager  = numberPassager