from payment import Payment

class Cash(Payment):
    number = int
    cvv = int 
    date = str
    
    """ Constructor de herencia"""
    def __init__(self, id, ammount, number, cvv, date):
        super.__init__(id, ammount)
        self.number = number
        self.cvv    = cvv
        self.date   = date
