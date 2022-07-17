from Razon import Razon
from datos_tipo_cliente.cliente import Cliente
#from evento import Evento

class RazonCompraDolar(Razon):
    def resolver(self, cliente:Cliente,evento:Evento) -> str:
        if not cliente.puefe_comprar_dolar():
            return "Este tipo de cliente no puede comprar dolares"

        if evento.monto>evento.saldoEnCuenta:
            return "Saldo Insuficiente para comprar los dolares"