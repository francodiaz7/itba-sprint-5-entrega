import json
from datos_tipo_cliente.cliente_black import ClienteBlack
from datos_tipo_cliente.cliente_gold import ClienteGold
from datos_tipo_cliente.cliente_classic import ClienteClassic
from datos_tipo_cliente.cuenta import Cuenta
from datos_tipo_cliente.cliente import Cliente
from evento import Evento

class Parser(object):
    def ejecutar(self, nombre_archivo: str) -> tuple[Cliente, 'list[Evento]']:
        #Crea una lista vacía donde van a ir las operaciones que se realicen
        operaciones = []
        with open (nombre_archivo) as jsonFile:
            eventos = json.load(jsonFile)
            cliente = self.analizarCliente(eventos)
            for operacion in operaciones:
                operaciones.append(Evento(**operacion))
        return cliente, operaciones

    #Recibe los datos de la clase Cliente
    def analizarCliente(self, datos):
        #Hay que poner que en otra clase diga el tipo de datos
        tipo = datos['tipo']
        if tipo == 'classic':
            cliente = ClienteClassic
        elif tipo == 'gold':
            cliente = ClienteGold
        elif tipo == 'black':
            cliente = ClienteBlack