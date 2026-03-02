class Agua:
    def __init__(self):
        self.temperatura = 20
        self.estado = "Fría"
        
    def get_temperatura(self):
        return self.temperatura
    
    def hervir(self):
        if self.temperatura < 100:
            self.temperatura += 20
            
            if self.temperatura >= 100:
                self.temperatura = 100
                self.estado = "Hirviendo"
            else:
                self.estado = "Calentándose"
            
    def get_estado(self):
        return self.estado
            
    def esta_hirviendo(self):
        return self.temperatura == 100
            
    def mostrar_info(self):
        return f"Agua Temperatura: {self.temperatura}, Estado: {self.estado}"