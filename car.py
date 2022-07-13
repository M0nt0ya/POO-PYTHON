from account import Account


class Car :
    id       = int
    """ Tipo de dato cambiado a base a ACCOUNT """
    driver   = Account ("","")
    passager = int
    """ brand    = str
    model    = str """
    license  = str
    
    
    """ Constructor """
    def __init__(self, license, driver):
        self.license     = license
        self.driver      = driver
        

    