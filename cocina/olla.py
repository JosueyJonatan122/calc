class Olla:
    def __init__(self):
        self.contenido = []
        self.agua = None
        
    def agregar_ingrediente(self, ingrediente):
        if ingrediente.esta_listo():
            self.contenido.append(ingrediente)    
        else:
            print("El ingrediente no está listo")
            
    def agregar_agua(self, agua):
        self.agua = agua
        
    def tiene_agua_hirviendo(self):
        if self.agua is not None:
            return self.agua.esta_hirviendo()
        return False
        
    def esta_lista(self):
        return len(self.contenido) >= 2 and self.tiene_agua_hirviendo()
        
    def mostrar_contenido(self):
        nombres = []
        for item in self.contenido:
            nombres.append(item.nombre_vege)
        return nombres