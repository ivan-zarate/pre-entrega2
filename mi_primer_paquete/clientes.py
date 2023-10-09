import json

class Cliente:
    
   def __init__(self, usuario, edad, contrasena):
      self.usuario= usuario
      self.edad= edad
      self.contrasena= contrasena
   def __str__(self):
          return f"\nGracias por registrarte {self[0]['usuario']}\n"
           
   def dataBase(data):
        with open("clientes.json", "w") as file:
          json.dump(data, file)
          file.write('\n')
    
     
   def ver_informacion():
     with open("clientes.json", "r") as file:
        clients = file.readlines()
        for client in clients:
            client_dict = json.loads(client)
            print("\nUsuarios registrados: \n")
        for x in client_dict:
            print(f"Nombre: {x['usuario']}")
            print(f"Edad: {x['edad']}")
            print('\t')
        
        
   def login(usuario, contrasena):
      try:
        with open("clientes.json", "r") as file:
          clients = file.readlines()
          for client in clients:
              client_dict = json.loads(client)
          for x in client_dict:
              if x['usuario'] == usuario:
                  if x['contrasena']==contrasena:
                      return f"\nBienvenid@ {usuario} !\n "
                  else:
                      return "\nLa contraseña ingresada no es correcta\n" 
      except:
              print('An exception occurred')
              
   def comprar(carrito):
      total=0
      for product in carrito:
        print(product)
        total+=product['precio']          
      print (f"El total a pagar es de ${total} \n")

