from datos_tipo_cliente.cliente import Cliente

#Deriva de la clase Cliente
class ClienteGold(Cliente):
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
        costo_transferencias = 0.05
        return monto * costo_transferencias

    def autorizacionTransferencia(self):
        return True