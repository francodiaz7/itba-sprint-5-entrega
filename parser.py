import json
from math import inf
from datos_tipo_cliente.cliente_black import ClienteBlack
from datos_tipo_cliente.cliente_gold import ClienteGold
from datos_tipo_cliente.cliente_classic import ClienteClassic
from datos_tipo_cliente.cuenta import Cuenta
from datos_tipo_cliente.cliente import Cliente
from evento import Evento

class Parser(object):
    def ejecutar(self, nombre_archivo: str) -> tuple[Cliente,'list[Evento]']:
        #Crea una lista vacía donde van a ir las operaciones que se realicen
        transacciones = []
        with open (nombre_archivo) as jsonFile:
            eventos = json.load(jsonFile)
            cliente = self.analizarCliente(eventos)
            for tr in transacciones:
                transacciones.append(Evento(**tr))
        return cliente, transacciones

    def analizarCliente(self, datos):
        tipo = datos['tipo']
        if tipo == 'CLASSIC':
            cliente = ClienteClassic
            limite_extraccion_diario = 10000
            limite_transferencia_recibida = 150000
            costo_transferencias = 0.1
            total_tarjetas_credito = 0
            total_chequeras = 0
        elif tipo == 'GOLD':
            cliente = ClienteGold
            limite_extraccion_diario = 20000
            limite_transferencia_recibida = 500000
            costo_transferencias = 0.05
            total_tarjetas_credito = 1
            total_chequeras = 1
        elif tipo == 'BLACK':
            cliente = ClienteBlack
            limite_extraccion_diario = 100000
            limite_transferencia_recibida = inf
            costo_transferencias = 0
            total_tarjetas_credito = 5
            total_chequeras = 2