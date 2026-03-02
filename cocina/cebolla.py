from ingredientes import Ingredientes

class Cebolla(Ingredientes):
    
    def __init__(self):
        super().__init__("Cebolla", 100)
        
    def imprimir_info(self):
        estado = "cruda"
        
        if self.get_vida_vege() == 0:
            estado = "Lista"
            
        info = super().ver_info()
        info += "estado: " + estado
        return info