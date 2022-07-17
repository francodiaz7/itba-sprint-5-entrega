class Evento:
    def __init__(self, **eventos):
        self.RETIRO_EFECTIVO_CAJERO_AUTOMATICO = eventos.get('RETIRO_EFECTIVO_CAJERO_AUTOMATICO')
        self.ALTA_TARJETA_CREDITO = eventos.get('ALTA_TARJETA_CREDITO')
        self.ALTA_CHEQUERA = eventos.get('ALTA_CHEQUERA')
        self.COMPRAR_DOLAR = eventos.get('COMPRAR_DOLAR')
        self.TRANSFERENCIA_ENVIADA = eventos.get('TRANSFERENCIA_ENVIADA')
        self.TRANSFERENCIA_RECIBIDA = eventos.get('TRANSFERENCIA_RECIBIDA')