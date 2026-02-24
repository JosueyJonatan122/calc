from tomate import Tomate
from cebolla import Cebolla
from cuchillo import Cuchillo
from pasta import Pasta
from agua import Agua
from olla import Olla

tomate= Tomate()
cebolla=Cebolla()
cuchillo=Cuchillo()
pasta= Pasta()
agua=Agua()
olla=Olla()

print(tomate.mostrar_info())
print(cebolla.mostrar_info())
print(cuchillo.mostrar_info())
print(pasta.mostrar_info())
print(agua.mostrar_info())
print(olla.mostrar_info())

print("Cortar ingredientes")

cuchillo.cortar(tomate)
cuchillo.cortar(cebolla)

print(tomate.mostrar_info())
print(cebolla.mostrar_info())
print(cuchillo.mostrar_info())

print("Afilar cuchillo")

cuchillo.afilar()
print(cuchillo.mostrar_info)

print("Hervir agua")

agua.hervir()
print(agua.mostrar_info())

print("Cocinar pasta")

pasta.cocinar()
print(pasta.mostrar_info())

print("Agregar a la olla")

olla.agregar(tomate)
olla.agregar(cebolla)
olla.agregar(pasta)

print(olla.mostrar_info())