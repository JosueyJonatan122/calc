class Parqueadero:
    def __init__(self,puesto,fecha_entrada,hora_entrada,estado="Ocupado"):
        self.puesto=puesto
        self.fecha_entrada = fecha_entrada
        self.hora_entrada = hora_entrada
        self.hora_salida = None
        self.estado = estado
        
    def registrar_salida(self,hora_salida):
        self.hora_salida=hora_salida
        self.estado="Disponible"
        
    def mostrar_info(self):
        print(f"Puesto: {self.puesto}")
        print(f"Fecha entrada: {self.fecha_entrada}")
        print(f"Hora entrada: {self.hora_entrada}")
        print(f"Hora salida: {self.hora_salida}")
        print(f"Estado: {self.estado}")