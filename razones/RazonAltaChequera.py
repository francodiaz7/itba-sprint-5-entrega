from Razon import Razon
from datos_tipo_cliente.cliente import Cliente
from evento import Evento

class RazonAltaChequera(Razon):
    def resolver(self,cliente:Cliente,evento:Evento)-> str:
        if not cliente.puede_crear_chequera():
            return "Al tipo de cliente sin acceso a chequeras"
        
        if cliente.cuenta.total_chequeras<(evento.totalChequerasActualemente+1):
            return "Tiene el maximo de cheuqueras permitidas"