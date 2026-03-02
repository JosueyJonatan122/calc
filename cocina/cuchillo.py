class Cuchillo:
    def __init__(self):
        self.nombre = "Cuchillo"
        self.filo = 100
        
    def get_nombre(self):
        return self.nombre
    
    def get_filo(self):
        return self.filo
    
    def cortar(self, ingrediente):
        if self.filo > 0:
            ingrediente.recibir_corte(25)
            self.recibir_desgaste(10)
        else:
            print("El cuchillo no tiene filo.")
    
    def recibir_desgaste(self, desgaste):
        self.filo -= desgaste
        if self.filo < 0:
            self.filo = 0 
    
    def afilar(self):
        self.filo = 100
        
    def mostrar_info(self):
        return f"Cuchillo Filo: " + str(self.filo)