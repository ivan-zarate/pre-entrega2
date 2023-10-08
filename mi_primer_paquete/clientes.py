class Cliente:
    
   def __init__(self, usuario, edad, contrasena):
     self.usuario= usuario
     self.edad= edad
     self.contrasena= contrasena

   def __str__(self) -> str:
          return f"Nombre: {self.usuario}"


