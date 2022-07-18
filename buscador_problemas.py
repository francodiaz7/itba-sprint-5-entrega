from datos_tipo_cliente.cliente import Cliente


class buscadorProblema(Cliente):

    def getResultado(self, datos):
        if datos.get('estado') == "ACEPTADA":
            return datos
        if datos.get('estado') == "RECHAZADA":
            #Faltaría conectar con las razones
            return datos