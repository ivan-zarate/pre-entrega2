from mi_primer_paquete.clientes import *

data=[]
productos=[{'producto':'Pera', 'precio':80},
           {'producto':'Manzana', 'precio':90}, 
           {'producto':'Banana', 'precio':120}, 
           {'producto':'Frutilla', 'precio':150}]
carrito=[]

def mostrar_menu():
    print("1. Registro")
    print("2. Login")
    print("3. Ver registro de contactos")
    print("4. Comprar")
    print("5. Salir")

def validar_opcion(opcion):
    return opcion in ['1', '2', '3', '4', '5']

def registro():  
    Cliente.usuario=input("Ingrese su nombre: ")
    Cliente.edad=int(input("Ingrese su edad: "))
    Cliente.contrasena=input("Ingrese su contraseña: ")
    data.append({
        'usuario':Cliente.usuario,
        'edad':Cliente.edad,
        'contrasena':Cliente.contrasena,
    })
    Cliente.dataBase(data)
    print(Cliente.__str__(data))
    return Cliente.usuario

def mostrarProductos():
    while True:
        print("1. Pera $80")
        print("2. Manzana $90")
        print("3. Banana $120")
        print("4. Frutilla $150")
        print("5. Finalizar compra")
        producto = input("Seleccione una opción: \t")
        if validar_opcion(producto):
            if producto== '1':
                carrito.append(productos[0])
            elif producto== '2':
                carrito.append(productos[1])
            elif producto== '3':
                carrito.append(productos[2])
            elif producto== '4':
                carrito.append(productos[3])
            elif producto== '5':
                Cliente.comprar(carrito)
                break
        else:
            print("Opción inválida. Intente nuevamente.")        