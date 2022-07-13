from payment import Payment

class Cash(Payment):
    
    """ Constructor de herencia"""
    def __init__(self, id, ammount):
        super.__init__(id, ammount)
