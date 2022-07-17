'''CREO QUE ESTO NO HACE FALTA'''


class Cuenta(object):
    def __init__(self, **cuenta):
        #cuenta.get() para extraer los valores y poder usar **cuenta
        #Se ahorra escritura, sino hay que copiar cada argumento en el constructor
        self.limite_extraccion_diario = cuenta.get('limite_extraccion_diario')
        self.limite_transferencia_recibida = cuenta.get('limite_transferencia_recibida')
        self.costo_transferencias = cuenta.get('costo_transferencias')
        self.saldo_descubierto_disponible = cuenta.get('saldo_descubierto_disponible')
        self.total_tarjetas_credito = cuenta.get('total_tarjetas_credito')
        self.total_chequeras = cuenta.get('total_chequeras')
