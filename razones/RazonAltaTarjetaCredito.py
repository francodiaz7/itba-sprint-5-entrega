from Razon import Razon
from datos_tipo_cliente.cliente import Cliente
from evento import Evento

class RazonAltaTarjetaCredito(Razon):
    def resolver(self,cliente:Cliente,evento:Evento)-> str:
        if not cliente.puedeTenerTarjetaDeCredito():
            return "Este tipo de cliente no puede tener tarjeta de credito"
        
        if cliente.cuenta.total_chequeras<(evento.totalTarjetasDeCreditoActualmente+1):
            return "Tiene el maximo de tarjetas de credito permitidas"