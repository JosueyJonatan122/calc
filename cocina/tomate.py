from ingredientes import Ingredientes

class Tomate(Ingredientes):
    
    def __init__(self):
        super().__init__("Tomate", 100)

    def imprimir_info(self):
        estado = "Crudo"
        
        if self.get_vida_vege() == 0:
            estado = "Listo"
            
        info = super().ver_info()
        info += "estado: " + estado
        return info