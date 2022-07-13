from account import Account
from car import Car

if __name__ == "__main__":
    print("Datos")

    car = Car( "PBD5555", Account("Andres", "1226902438"))
    print(vars(car))
    print(vars(car.driver))



    """ from account import Account
    from car import Car
    from driver import Driver
    from payment import Payment
    from route import Route
    from user import User
    
    
    caro = Car()
    caro.id          = 5
    caro.brand       = "NombreCarro"
    caro.driver      = "Nombre"
    caro.passanggers =  5    
    
    cuenta = Account ()
    cuenta.id       = 10 
    cuenta.name     = "Pacifico"
    cuenta.document = "Debito"
    cuenta.mail     = "nombrepepito@"
    cuenta.password = "ABCDF"
    
    conductor = Driver()
    conductor.id        = 11
    conductor.name      = "Juan"
    conductor.document  = "123456789"
    conductor.mail      = "juancarlos@"
    conductor.password  = "juan123"
    
    pago = Payment ()
    pago.id      = 123
    pago.ammount = 21
    
    
    ruta = Route ()
    ruta.id   = 1
    ruta.start  = "Jueves 7am"
    ruta.end    = "Jueves 5pm"
    
    usuario = User()
    usuario.id       =42
    usuario.name     ="Andres"
    usuario.document ="1726902438"
    usuario.email    ="andres123@"
    usuario.password ="1726Andres"
    
print (vars(cuenta))
print (vars(conductor))
print (vars(pago))
print (vars(ruta))
print (vars(usuario)) 
print (vars(caro)) """