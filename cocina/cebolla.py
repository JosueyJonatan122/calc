class Cebolla:
    def __init__(self):
        self.vida = 100
        
    def recibir_corte(self):
        self.vida -= 25
        if self.vida < 0:
            self.vida = 0
            
    def esta_viva(self):
        return self.vida > 0
    
    def mostrar_info(self):
        return (f"Cebolla - Vida {self.vida}%")
        