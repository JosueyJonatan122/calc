class Usuario:
    
   def __init__(self):
      self.cedula = cedula
      self.nombre = nombre

   def get_cedula(self):
      return self.cedula
 
   def set_cedula(self,nueva_cedula):
       self.cedula = nueva_cedula

   def imprimir_datos(self):
      print (f"nombre cliente: {self.nombre}")
      print (F"cedula cliente: {self.cedula}")