import email
from re import S
from unicodedata import name
from xml.dom.minidom import Document


class Driver:
    id        = int
    name      = str
    document  = str
    email     = str
    password  = str