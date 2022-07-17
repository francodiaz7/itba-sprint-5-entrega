from Razon import Razon
from datos_tipo_cliente.cliente import Cliente
from evento import Evento

class RazonRetiroEfectivoBlack(Razon):
    def resolver(self, cliente:Cliente,evento:Evento) -> str:
        if cliente.cuenta.limite_extraccion_diario<evento.monto:
            return "La extraccion supera el monto de extraccion permitido"

        if evento.monto>(evento.saldoEnCuenta+cliente.cuenta.saldo_descubierto_disponible):
            return "Saldo Insuficiente para retiro solicitado"