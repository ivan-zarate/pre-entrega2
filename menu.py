from mi_primer_paquete.clientes import *

data=[]

def mostrar_menu():
    print("1. Registro")
    print("2. Ver información de contacto")
    print("3. Salir")

def validar_opcion(opcion):
    return opcion in ['1', '2', '3']

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
    print(Cliente)

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if validar_opcion(opcion):
        if opcion == '1':
                registro()
        elif opcion == '2':
                Cliente.ver_informacion()
        else:
                print("¡Hasta luego!")
                break
    else:
        print("Opción inválida. Intente nuevamente.")
   
   

#print(Cliente.ver_informacion())