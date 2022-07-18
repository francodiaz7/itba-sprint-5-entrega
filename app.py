from procesador_html import ProcesadorHtml
from parser import Parser
from buscador_problemas import buscadorProblema


if __name__ == '__main__':
    ruta = 'ejemplos_json/eventos_black.json'
    parser = Parser()
    cliente,eventos = parser.ejecutar(ruta)
    salidaHtml = ProcesadorHtml()
    buscador = buscadorProblema(cliente)
    for e in eventos:
        # salidaHtml.append(buscador.getResultado(e))
        salidaHtml.append(e)
    
    salidaHtml.crear_html(cliente)