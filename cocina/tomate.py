class Tomate:
    def __init__(self):
        self.vida=100
        
    def recibir_corte(self):
        self.vida-= 20
        if self.vida < 0:
            self.vida = 0
            
    def esta_vivo(self):
        return self.vida > 0
    
    def mostrar_info(self):
        return (f"Tomate - Vida: {self.vida}%")
    