
class ClienteGold():
    def __init__(self, cliente):
        self.nombre = cliente['nombre']
        self.apellido = cliente['apellido']
        self.numero = cliente['numero']
        self.dni = cliente['dni']
        self.direccion = cliente['direccion']
        self.limite_extraccion_diario = 20000
        self.limite_transferencia_recibida = 500000
        self.costo_transferencias =0.05
        self.saldo_descubierto_disponible =0
        self.total_tarjetas_credito =1
        self.total_chequeras =1
    

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
        return True