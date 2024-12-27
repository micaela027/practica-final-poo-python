class Mascota:
    def __init__(self, nombre, edad, salud, precio):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.precio = precio
    
    def actualizar_informacion(self, edad = None, salud=None, precio=None):
        if edad:
            self.edad = edad
        if salud:
            self.salud = salud
        if precio:
            self.precio = precio
    
    def mostrar_informacion(self):
        return f"Mascota: {self.nombre}, Edad: {self.edad}, Salud: {self.salud}, Precio: {self.precio}"
    
class Perro(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, nivel_energia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.nivel_energia = nivel_energia
    
    def mostrar_caracteristicas(self):
        return f"Raza: {self.raza}, Nivel de Energia: {self.nivel_energia}"

class Gato(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, independencia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.independencia = independencia

    def mostrar_caracteristicas(self):
        return f"Raza: {self.raza}, Independencia: {self.independencia}"

class Serpiente(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, veneno):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.veneno = veneno

    def mostrar_caracteristicas(self):
        return f"Tipo: {self.tipo}, Veneno: {self.veneno}"
    
class Ave(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, vuelo):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.vuelo = vuelo
    
    def mostrar_caracteristicas(self):
        return f"Raza: {self.raza}, Vuelo: {self.vuelo}"