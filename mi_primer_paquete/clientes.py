import json

class Cliente:
    
   def __init__(self, usuario, edad, contrasena):
    try:
      self.usuario= usuario
      self.edad= edad
      self.contrasena= contrasena
    except :
      print('An exception occurred')
      
   def __str__(self) -> str:
          return f"Gracias por registrarse: {self.usuario}"
           
   def dataBase(data):
        with open("clientes.json", "w") as file:
          json.dump(data, file, indent=4)
          file.write('\n')
     
   
        
   def ver_informacion():
     with open("clientes.json", "r") as file:
        contactos = file.readlines()
        for contacto in contactos:
            contacto_dict = json.loads(contacto)
            formatContact=contacto_dict['cliente'][0]
            print("Información del contacto:")
            print(f"Nombre: {formatContact['usuario']}")
            print(f"Edad: {formatContact['edad']}")
            print(f"Contraseña: {formatContact['contrasena']}")
            return 
        
   """def registro(usuario, contrasena):
      try:
          clientes[usuario]=contrasena
          return usuario
      except:
        print('An exception occurred')"""
        
        
   """def login(usuario, contrasena):
      try:
          for k in clientes.keys():
              if k == usuario:
                  if clientes[usuario]==contrasena:
                      return f"Bienvenido {usuario} !"
                  else:
                      return "La contraseña ingresada no es correcta"
      except:
              print('An exception occurred')
              
              
   def update(usuario):
      try:
          newPass=input("Ingrese su nueva contraseña: ")
          for k in clientes.keys():
              if k == usuario:
                  clientes[usuario]=newPass
                  return "Se ha guardado su nueva contraseña"
      except:
        print('An exception occurred')"""


