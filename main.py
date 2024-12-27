#Funciones para la interfaz de consola:
from clases.cliente import Cliente
from clases.inventario import Inventario
from clases.mascota import Ave, Gato, Perro, Serpiente
from clases.producto import Producto
from clases.venta import Venta


def registar_mascota():
    tipo = input ("Ingrese el tipo de mascota (Perro/Gato/Serpiente/Ave) ").strip().lower()
    nombre = input ("Ingrese el nombre de la mascota: ")
    edad = int(input("Edad de la mascota: "))
    salud = input("Estado de salud de la mascota: ")
    precio = float(input("El precio de la mascota: "))

    if tipo == "perro":
        raza = input("Raza del perro: ")
        nivel_energia = input("Nivel de energia del perro: ")
        mascota = Perro(nombre, edad, salud, precio, raza, nivel_energia)
    elif tipo == "gato":
        raza = input("Raza del gato: ")
        independencia = input("Nivel de independencia del gato: ")
        mascota = Gato(nombre, edad, salud, precio, raza, independencia)
    elif tipo == "serpiente":
        raza = input("Raza de la serpiente: ")
        veneno = input("Veneno de la serpiente: ")
        mascota = Serpiente(nombre, edad, salud, precio, raza, veneno)
    elif tipo == "ave":
        raza = input("Raza del ave: ")
        vuelo = input("Vuelo del ave: ")
        mascota = Ave(nombre, edad, salud, precio, raza, vuelo)
    else: 
        print("Tipo de mascota no reconocida")
        return
    
    return mascota

def registrar_cliente():
    nombre = input("Nombre del cliente: ").lower()
    direccion = input("Direccion del cliente: ").lower()
    telefono = input("Telefono del cliente: ").lower()
    cliente = Cliente(nombre, direccion, telefono)
    return cliente

def registrar_producto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoria del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad de productos: "))
    producto = Producto(nombre, categoria, precio, cantidad)
    return producto

def registrar_venta(clientes, inventario):
    nombre_cliente = input("Nombre del cliente: ")
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)
    if not cliente:
        print("Cliente no encontrado")
        return
    
    productos = []

    while True:
        nombre_producto = input("Nombre del producto (deje vacio para finalizar): ")
        if not nombre_producto:
            break
        producto = next((p for p in inventario.lista_productos if p.nombre == nombre_producto), None)
        if producto:
            productos.append(producto)
        else:
            print("Producto no encontrado")
    
    if productos:
        venta = Venta(cliente, productos)
        venta.registrar_venta()
        print("La venta ha sido registrada con exito")
    else:
        print("No se han registrado productos para la venta")

def mostrar_menu():
    print("/n --- Menu de gestión de Patas Felices ---")
    print("1. Registrar mascota")
    print("2. Registrar cliente")
    print("3. Registrar producto")
    print("4. Registrar venta")
    print("5. Mostrar informacion acerca de mascotas")
    print("6. Mostrar informacion acerca de clientes")
    print("7. Mostrar informacion acerca de productos")
    print("8. Generar alerta de inventario")
    print("9. Salir")

def main():
    mascotas = []
    clientes = []
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input ("Selecciones una opcion: ")

        if opcion == "1":
            mascota = registar_mascota()
            if mascota:
                mascotas.append(mascota)
                print("Mascota registrada con exito")
        elif opcion == "2":
            cliente = registrar_cliente()
            if cliente:
                clientes.append(cliente)
                print("Cliente registrado con éxito")
        elif opcion == "3":
            producto = registrar_producto()
            if producto:
                inventario.agregar_producto(producto)
                print("Producto registrado con éxito")
        elif opcion == "4":
            registrar_venta(clientes, inventario)
        elif opcion == "5":
            for mascota in mascotas:
                print(mascota.mostrar_informacion())
                if isinstance(mascota, Perro) or isinstance (mascota, Gato) or isinstance(mascota, Serpiente) or isinstance(mascota, Ave):
                    print(mascota.mostrar_caracteristicas())
        elif opcion == "6":
            for cliente in clientes:
                print(cliente.mostrar_informacion())
        elif opcion == "7":
            for producto in inventario.lista_productos:
                print(producto.mostrar_informacion())
        elif opcion == "8":
            umbrar_minimo = int(input("Ingrese el umbral minimo del inventario: "))
            print(inventario.generar_alerta(umbrar_minimo))
        elif opcion == "9":
            print("Saliendo del sistema, gracias por elegir Patas Felices")
        else:
            print("Opcion no valida. Intente nuevamente")

if __name__ == "__main__":
    main()









