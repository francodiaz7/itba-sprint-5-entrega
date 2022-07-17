from datos_tipo_cliente.cliente import Cliente

#Deriva de la clase Cliente
class ClienteClassic(Cliente):
    def __init__(self, **cliente):
        Cliente.__init__(**cliente)

    def puedeCrearChequera(self):
        return True

    def puedeTenerTarjetaDeCredito(self):
        return True

    def puedeComprarDolar(self):
        return True