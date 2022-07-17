from datos_tipo_cliente.cliente import Cliente


class ProcesadorHtml:

    def __init__(self) -> None:
        self.elementos = []

    def append(self, elemento:dict):
        self.elementos.append(elemento)

    def crear_html(self, cliente: Cliente):
        transacciones = ""
        for e in self.elementos:
            transacciones += "<br><td>{fecha}</td><td>{tipo}</td><td>{estado}</td><td>{monto}</td><td>{razon}</td>".format(
            fecha = e['fecha'],
            tipo = e['tipo'].replace("_", " "),
            estado = e['estado'],
            monto = e['monto'],
            razon = e['razon']
            )
        html = """
            <html>
                <title>Listado de transacciones</title>
                <body>
                    <h1>{apellido}, {nombre}</h1>
                    <div>Número cliente: {numero}</div>
                    <div>DNI: {dni}</div>
                    <div>Dirección: {direccion}</div>
                    <table>
                        <tr><td>Fecha</td><td>Tipo</td><td>Estado</td><td>Monto></td><td>Razon</td></tr>
                        {ftransacciones}
                    </table>
                </body>
            </html>
            """.format(
                    direccion = str(cliente.direccion),
                    numero = cliente.numero,
                    nombre = cliente.nombre,
                    apellido = cliente.apellido, 
                    dni = cliente.dni,
                    ftransacciones = transacciones
                    )

        archivo = open("index.html", "w")
        archivo.write(html)
        archivo.close()