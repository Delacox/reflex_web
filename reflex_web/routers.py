from enum import Enum

class Route(Enum):
    INDEX = "/"
    ABOUT_US = "/nosotros"
    PRICES = "/precios"
    CONTACT = "/contacto"
    
    SIGNUP = "/registro"
    LOGIN = "/login"
    
    