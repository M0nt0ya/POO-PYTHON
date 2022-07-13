from unicodedata import name
from xml.dom.minidom import Document


class Account :
    id       = int 
    name     = str
    document = int
    mail     = str
    password = str
    
    """ Constructor """
    def __init__(self, name, document):
        self.name      = name
        self.document  = document
        