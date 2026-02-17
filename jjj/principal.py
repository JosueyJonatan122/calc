from cliente import Usuario
from numeros import Numero
from resultados import calcularoda   # usa el nombre exacto de tu clase

# Crear usuario
usuario = Usuario()

# Crear numeros
num1 = Numero(5)
num2 = Numero(10)

# Crear calculadora
obj_calc = calcularoda("suma", 0, "17/02/2026")

# Realizar operacion
dato = obj_calc.realizar_operacion(num1, num2)

print("Resultado final:", dato)
