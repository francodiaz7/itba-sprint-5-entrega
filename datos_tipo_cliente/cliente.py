from datos_tipo_cliente.direccion import Direccion
from datos_tipo_cliente.cuenta import Cuenta
class Cliente(object):
    #El doble asterisco (**, **kwargs) se usa cuando no conoces la cantidad de 
    # argumentos que vas a pasar o si son varios. Recibe un diccionario
    # de argumentos.
    def __init__(self, **cuenta):
        self.cuenta = Cuenta(**cuenta)
    
    def gestionarDatos(self, datos):
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.numero = datos['numero']
        self.dni = datos['dni']
        self.direccion = Direccion(**datos['direccion'])
    
    def puedeCrearChequera(self):
        return False

    def puedeTenerTarjetaDeCredito(self):
        return False

    def puedeComprarDolar(self):
        return False

    def tieneCuentaCorriente(self):
        return False

    def comisionTransferencia(self, monto: int):
        return monto * self.cuenta.costo_transferencias

    def autorizacionTransferencia(self):
        return True

