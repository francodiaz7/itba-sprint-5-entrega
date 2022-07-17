from datos_tipo_cliente.cliente import Cliente
from datos_tipo_cliente.cuenta import Cuenta

class ClienteBlack(Cliente):
    def __init__(self, **cliente):
        Cliente.__init__(**cliente)

    def puedeCrearChequera(self):
        return True

    def puedeTenerTarjetaDeCredito(self):
        return True

    def puedeComprarDolar(self):
        return True

    def tieneCuentaCorriente(self):
        return True

    def comisionTransferencia(self, monto: int):
        return monto * self.cuenta.costo_transferencias

    def autorizacionTransferencia(self):
        return False