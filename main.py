from mi_primer_paquete.clientes import *
from mi_primer_paquete.menu import *


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: \t")

    if validar_opcion(opcion):
        if opcion == '1':
                registro()
        elif opcion == '2':
                usuario=input("\nIngrese su usuario: ").capitalize()
                contrasena=input("Ingrese su contrasena: ")
                result=Cliente.login(usuario, contrasena)
                if result==None:
                    print("\nEl usuario no se encuentra registrado\n")
                else:
                    print(result)    
        elif opcion == '3':
                Cliente.ver_informacion()
        elif opcion == '4':
                mostrarProductos()        
        else:
                print("¡Hasta luego!")
                break
    else:
        print("Opción inválida. Intente nuevamente.")
   
   