from datetime import datetime
from shlex import join


class Venta:
    def __init__(self, cliente, lista_producto):
        self.cliente = cliente
        self.lista_producto = lista_producto
        self.fecha = datetime.now()
        self.total = self.calcular_total()

    def calcular_total(self):
        return sum(producto.precio for producto in self.lista_producto)
    
    def registrar_venta(self):
        self.cliente.registrar_compra(self)
        return f"Venta Registrada: {self.mostrar_informacion()}"
    
    def mostrar_informacion(self):
        productos = ", ", join([producto.nombre for producto in self.lista_producto])
        return f"Cliente: {self.cliente.nombre}, Productos: {productos}, Total: {self.total}"