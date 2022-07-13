from car import Car

class UberPromo(Car):
    brand   = str
    model   = str
    """ Constructor """
    
    def __init__(self, license, driver, brand, model):
        super.__init__(license, driver)
        self.brand  = brand
        self.model  = model