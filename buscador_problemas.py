from datos_tipo_cliente.cliente import Cliente
from razones.Razon import Razon

class buscadorProblema(Cliente):
    def getResultado(self, datos):
        motivo = "analizar"
        if datos.get('estado') == "ACEPTADA":
            return datos
        if datos.get('estado') == "RECHAZADA":
            #Faltaría conectar con las razones
            motivo = "Analizar"
            datos['razon'] = motivo