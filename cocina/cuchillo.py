class Cuchillo:
    def __init__(self):
        self.filo = 100
        
    def cortar(self, ingrediente):
        if self.filo <= 0:
            print("el cuchillo no tiene filo, debes afilarlo")
            return
        
        ingrediente.recibir_corte()
        self.filo -= 10
        
        if self.filo < 0:
            self.filo = 0
            
        
    def afilar(self):
        self.filo = 100
        
    def mostrar_info(self):
        return (f"Cuchillo - Filo {self.filo}%")
    
    