class Parqueadero:
    def __init__(self, puesto, fecha_entrada, hora_entrada, estado="Ocupado"):
        self.__puesto = puesto
        self.__fecha_entrada = fecha_entrada
        self.__hora_entrada = hora_entrada
        self.__hora_salida = None
        self.__estado = estado

    # SETTERS
    def set_puesto(self, puesto):
        self.__puesto = puesto

    def set_fecha(self, fecha):
        self.__fecha_entrada = fecha

    def set_hora(self, hora):
        self.__hora_entrada = hora

    def set_estado(self, estado):
        self.__estado = estado

    # GETTERS
    def get_puesto(self):
        return self.__puesto

    def get_fecha(self):
        return self.__fecha_entrada

    def get_hora(self):
        return self.__hora_entrada

    def get_estado(self):
        return self.__estado

    def registrar_salida(self, hora_salida):
        self.__hora_salida = hora_salida
        self.__estado = "Disponible"

    def mostrar_info(self):
        return (f"Puesto: {self.__puesto}\n"
                f"Fecha entrada: {self.__fecha_entrada}\n"
                f"Hora entrada: {self.__hora_entrada}\n"
                f"Hora salida: {self.__hora_salida}\n"
                f"Estado: {self.__estado}")