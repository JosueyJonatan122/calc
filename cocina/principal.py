import tkinter as ventana
from tomate import Tomate
from cebolla import Cebolla
from cuchillo import Cuchillo
from pasta import Pasta
from agua import Agua
from olla import Olla

tomate = Tomate()
cebolla = Cebolla()
cuchillo = Cuchillo()
pasta = Pasta()
agua = Agua()
olla = Olla()

def cortar_tomate():
    if cuchillo.get_filo() > 0:
        cuchillo.cortar(tomate)
        mensaje.set("Cortando tomate...")
    else:
        mensaje.set("El cuchillo necesita afilarse")
    actualizar()

def cortar_cebolla():
    if cuchillo.get_filo() > 0:
        cuchillo.cortar(cebolla)
        mensaje.set("Cortando cebolla...")
    else:
        mensaje.set("El cuchillo necesita afilarse")
    actualizar()

def hervir_agua():
    agua.hervir()
    if agua.esta_hirviendo():
        mensaje.set("El agua está hirviendo 🔥")
    else:
        mensaje.set("Calentando agua...")
    actualizar()

def cocinar():
    if not agua.esta_hirviendo():
        mensaje.set("Primero debes hervir el agua")
        return

    if tomate.esta_listo() and cebolla.esta_listo():
        
        if not olla.esta_lista():
            olla.agregar_ingrediente(tomate)
            olla.agregar_ingrediente(cebolla)

        if not pasta.esta_lista():
            pasta.hervir()
            mensaje.set("La pasta se está cocinando...")
        else:
            mensaje.set("La pasta está lista 🍝")
    else:
        mensaje.set("Debes cortar todos los ingredientes primero")

    actualizar()

def servir():
    if pasta.esta_lista():
        mensaje.set("¡Combate culinario finalizado! La pasta ha sido servida con éxito 🍽")
    else:
        mensaje.set("La pasta aún no está lista")
    actualizar()

def afilar():
    cuchillo.afilar()
    mensaje.set("El cuchillo fue afilado")
    actualizar()

def actualizar():

    texto.set(
        "Tomate: " + str(tomate.get_vida()) + "\n" +
        "Cebolla: " + str(cebolla.get_vida()) + "\n" +
        "Temperatura Agua: " + str(agua.get_temperatura()) + "\n" +
        "Pasta: " + str(pasta.get_coccion()) + "\n" +
        "Filo cuchillo: " + str(cuchillo.get_filo())
    )

app = ventana.Tk()
app.title("Cocina Virtual - Combate Culinario")

texto = ventana.StringVar()
ventana.Label(app, textvariable=texto).pack()

mensaje = ventana.StringVar()
ventana.Label(app, textvariable=mensaje).pack()

ventana.Button(app, text="Cortar Tomate", command=cortar_tomate).pack()
ventana.Button(app, text="Cortar Cebolla", command=cortar_cebolla).pack()
ventana.Button(app, text="Hervir Agua", command=hervir_agua).pack()
ventana.Button(app, text="Cocinar Pasta", command=cocinar).pack()
ventana.Button(app, text="Afilar Cuchillo", command=afilar).pack()
ventana.Button(app, text="Servir", command=servir).pack()

actualizar()
app.mainloop()