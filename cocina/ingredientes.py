class Ingredientes:
    def __init__(self, nombre, vida):
        self.nombre_vege = nombre
        self.vida_vege = vida
        
    def get_vida(self):    
        return self.vida_vege
    
    def set_vida(self, nueva_vida):
        self.vida_vege = nueva_vida
        
    def recibir_corte(self, corte):
        vida_antes = self.vida_vege
    
        nueva = self.vida_vege - corte
    
        if nueva < 0:
            nueva = 0
        
        self.vida_vege = nueva
    
        dano_real = vida_antes - self.vida_vege
    
        print("Se realizó :", dano_real, "de daño al :", self.nombre_vege)
        print("Vida restante:", self.vida_vege, sep="\n")
        
    def esta_listo(self):
        return self.vida_vege == 0
    
    def ver_info(self):
        info: str = "nombre: " + self.nombre_vege + ", vida restante: " + str(self.vida_vege) + " "
        return info
           
        
        