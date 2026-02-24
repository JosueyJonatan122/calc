class Olla:
   def __init__(self):
        self.contenido = []
        
   def agregar (self, ingrediente):
       self.contenido.append(ingrediente)
        
    
   def mostrar_info(self):
        return (f"Olla tiene : {len(self.contenido)} ingredientes")