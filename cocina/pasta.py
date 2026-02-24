class Pasta:
    def __init__(self):
        self.coccion = 0 
        
    def cocinar(self):
        if self.coccion < 100:
            self.coccion += 20
            if self.coccion >100:
                self.coccion = 100
                
    def esta_lista (self):
        return self.coccion == 100
    
    def mostrar_info(self):
        return (f"Pasta - coccion {self.coccion}%")
    