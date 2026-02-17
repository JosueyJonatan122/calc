class Calcularoda:

    def __init__(self, tipo_operacion, resultado, fecha_uso):
        self.tipo_operacion = tipo_operacion
        self.resultado = resultado
        self.fecha_uso = fecha_uso
        self.texto_tabla=[]

    def calcular_suma(self, obj_num1, obj_num2):
        result_suma = obj_num1.get_num() + obj_num2.get_num()
        print(f"resultado suma: {result_suma}")
        return result_suma

    def calcular_resta(self, obj_num1, obj_num2):
        result_resta = obj_num1.get_num() - obj_num2.get_num()
        print(f"resultado resta: {result_resta}")
        return result_resta

    def calcular_multi(self, obj_num1, obj_num2):
        result_multi = obj_num1.get_num() * obj_num2.get_num()
        print(f"resultado multiplicacion: {result_multi}")
        return result_multi

    def calcular_division(self, obj_num1, obj_num2):
        result_division = obj_num1.get_num() / obj_num2.get_num()
        print(f"resultado division: {result_division}")
        return result_division

    def realizar_operacion(self, obj_num1, obj_num2):

        if self.tipo_operacion == "suma":
            dato = self.calcular_suma(obj_num1, obj_num2)

        elif self.tipo_operacion == "resta":
            dato = self.calcular_resta(obj_num1, obj_num2)

        elif self.tipo_operacion == "multiplicar":
            dato = self.calcular_multi(obj_num1, obj_num2)

        elif self.tipo_operacion == "division":
            dato = self.calcular_division(obj_num1, obj_num2)

        else:
            print("Operacion no valida")
            return None

        return dato


