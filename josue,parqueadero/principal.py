import tkinter as formulario
from carro import Carro
from parqueadero import Parqueadero
from usuario import Usuario

# =========================
# FUNCIONES
# =========================

def tomar_datos():
    # Usuario
    obj_usuario.set_nombre(entry_nombre.get())
    obj_usuario.set_cedula(entry_cedula.get())
    obj_usuario.set_tipo_usuario(entry_tipo.get())

    # Carro
    obj_carro.set_placa(entry_placa.get())
    obj_carro.set_marca(entry_marca.get())
    obj_carro.set_color(entry_color.get())

    # Parqueadero
    obj_parqueadero.set_puesto(entry_puesto.get())
    obj_parqueadero.set_fecha(entry_fecha_entrada.get())
    obj_parqueadero.set_hora(entry_hora_entrada.get())
    obj_parqueadero.set_estado("Ocupado")

    # Mostrar información
    lbl_resultado.config(
        text=obj_usuario.mostrar_info() + "\n\n" +
             obj_carro.mostrar_info() + "\n\n" +
             obj_parqueadero.mostrar_info()
    )


def salida():
    obj_parqueadero.registrar_salida(entry_hora_salida.get())

    lbl_resultado.config(
        text=obj_parqueadero.mostrar_info()
    )


# =========================
# OBJETOS VACÍOS
# =========================

obj_usuario = Usuario("", "", "")
obj_carro = Carro("", "", "")
obj_parqueadero = Parqueadero("", "", "", "")


# =========================
# VENTANA
# =========================

obj_ventana =formulario.Tk()
obj_ventana.title("Sistema Parqueadero")
obj_ventana.geometry("500x600")

frame_principal = formulario.Frame(obj_ventana)
frame_principal.pack(pady=10)


# =========================
# CAMPOS
# =========================

formulario.Label(frame_principal, text="Nombre").pack()
entry_nombre = formulario.Entry(frame_principal)
entry_nombre.pack()

formulario.Label(frame_principal, text="Cedula").pack()
entry_cedula = formulario.Entry(frame_principal)
entry_cedula.pack()

formulario.Label(frame_principal, text="Tipo Usuario").pack()
entry_tipo = formulario.Entry(frame_principal)
entry_tipo.pack()

formulario.Label(frame_principal, text="Placa").pack()
entry_placa = formulario.Entry(frame_principal)
entry_placa.pack()

formulario.Label(frame_principal, text="Marca").pack()
entry_marca = formulario.Entry(frame_principal)
entry_marca.pack()

formulario.Label(frame_principal, text="Color").pack()
entry_color = formulario.Entry(frame_principal)
entry_color.pack()

formulario.Label(frame_principal, text="Puesto").pack()
entry_puesto = formulario.Entry(frame_principal)
entry_puesto.pack()

formulario.Label(frame_principal, text="Fecha entrada").pack()
entry_fecha_entrada = formulario.Entry(frame_principal)
entry_fecha_entrada.pack()

formulario.Label(frame_principal, text="Hora Entrada").pack()
entry_hora_entrada = formulario.Entry(frame_principal)
entry_hora_entrada.pack()

formulario.Label(frame_principal, text="Hora Salida").pack()
entry_hora_salida = formulario.Entry(frame_principal)
entry_hora_salida.pack()




# =========================
# BOTONES
# =========================

boton_enviar= formulario.Button(frame_principal, text="Guardar info",
       command=lambda:tomar_datos()).pack(pady=5)


boton_salida=formulario.Button(frame_principal, text="Registrar Salida",
       command=lambda:salida()).pack(pady=5)






# =========================
# RESULTADO
# =========================

lbl_resultado = formulario.Label(frame_principal, text="", justify=formulario.LEFT)
lbl_resultado.pack(pady=10)


obj_ventana.mainloop()