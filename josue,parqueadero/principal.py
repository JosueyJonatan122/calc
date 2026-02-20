from usuario import Usuario
from carro import Carro
from parqueadero import Parqueadero

obj_usuario1=Usuario("Carlos", "10089027", "Cliente")
obj_carro1=Carro("GAY28K", "BMW", "Gris")
obj_parqueadero=Parqueadero("p1", "20/02/26", "6:59", "ocupado")
obj_usuario1.mostrar_info()
obj_carro1.mostrar_info()
obj_parqueadero.mostrar_info()
obj_parqueadero.registrar_salida("7:20")
obj_parqueadero.mostrar_info()