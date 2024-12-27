class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.historial_compra = []

    def actualizar_informacion (self, direccion, telefono):
        if direccion:
            self.direccion = direccion
        if telefono:
            self.telefono = telefono

    def registrar_compra (self, compra):
        self.historial_compra.append(compra)
    
    def mostrar_informacion(self):
        return f"El cliente es {self.nombre}, Direccion: {self.direccion}, Telefono {self.telefono}"
