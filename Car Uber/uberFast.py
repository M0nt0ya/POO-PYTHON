from car import Car

class UberFast(Car):
    brand      = str
    model      = str
    loadSize   = []
    loadWeigth = int
    """ Constructor """
    
    def __init__(self, license, driver, brand, model, loadSize, loadWeigth):
        super.__init__(license, driver)
        self.brand       = brand
        self.model       = model
        self.loadSize    = loadSize
        self.loadWeight  = loadWeigth
        