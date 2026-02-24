class Agua:
    def __init__(self):
        self.hirviendo = False
        
    def hervir(self):
        self.hirviendo =True
        
    def mostrar_info(self):
        return (f"Agua hirviendo: {self.hirviendo}")