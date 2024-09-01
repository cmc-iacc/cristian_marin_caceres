import tkinter as tk
from tkinter import messagebox

def registro_estudiantes():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    clase = entry_clase.get()
    seccion = entry_seccion.get()
    inscripccion = Var_estado_inscripcion.get()
    optativas = [var_ingles.get(), var_historia.get(), var_fisica.get()]
    comentarios = text_comentarios.get("1.0", tk.END).strip()
    nivel_escolar = var_nivel_escolar.get()
    
    mensaje = f'''Estudiante registrado:
    Nombre del Estudiante: {nombre}
    Apellido del Estudiante: {apellido}
    Edad del estudiante: {edad}
    Clase del Estudiante: {clase}
    Sección del Estudiante: {seccion}
    Estado de Inscripción: {inscripccion}
    Materias Optativas: {optativas}
    Comentarios: {comentarios}
    Nivel Escolar: {nivel_escolar}'''
    
    messagebox.showinfo("Registro Exitoso", mensaje)
    
    # Mostrar los detalles del estudiante en la terminal
    print("-----Detalles del estudiantes-----")
    print("Nombre: ", nombre)
    print("Apellido: ", apellido)
    print("Edad :", edad)
    print("Clase: ", clase)
    print("Sección", seccion)
    print("Estado de inscripción: ", inscripccion)
    print("Materias optativas: ", optativas)
    print("Comentarios: ", comentarios)
    print("Nivel Escolar: ", nivel_escolar)

def limpiar_formulario():
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_clase.delete(0, tk.END)
    entry_seccion.delete(0, tk.END)
    Var_estado_inscripcion.set(None)
    var_ingles.set(0)
    var_historia.set(0)
    var_fisica.set(0)
    text_comentarios.delete("1.0", tk.END)
    var_nivel_escolar.set("Primaria")

#Ventana principal
ventana = tk.Tk()
ventana.title("Regsitro de estudiantes InnovadoresX")

#Frames
frame_estudiante = tk.Frame(ventana)
frame_estudiante.pack(pady=10)

frame_academico = tk.Frame(ventana)
frame_academico.pack(pady=10)

frame_estado_inscripcion = tk.Frame(ventana)
frame_estado_inscripcion.pack(pady=10)

frame_optativas = tk.Frame(ventana)
frame_optativas.pack(pady=10)

frame_comentarios = tk.Frame(ventana)
frame_comentarios.pack(pady=10)


# Label para información del estudiante
label_nombre = tk.Label(frame_estudiante, text="Nombre del Estudiante:")
label_nombre.grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(frame_estudiante)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

label_apellido = tk.Label(frame_estudiante, text="Apelldio del Estudiante:")
label_apellido.grid(row=1, column=0, padx=5, pady=5)
entry_apellido = tk.Entry(frame_estudiante)
entry_apellido.grid(row=1, column=1, padx=5, pady=5)

label_edad = tk.Label(frame_estudiante, text="Edad del Estudiante:")
label_edad.grid(row=2, column=0, padx=5, pady=5)
entry_edad = tk.Entry(frame_estudiante)
entry_edad.grid(row=2, column=1, padx=5, pady=5)

# Label para detalles académicos
label_clase = tk.Label(frame_academico, text="Clase:")
label_clase.grid(row=0, column=0, padx=5, pady=5)
entry_clase = tk.Entry(frame_academico)
entry_clase.grid(row=0, column=1, padx=5, pady=5)

label_seccion = tk.Label(frame_academico, text="Sección:")
label_seccion.grid(row=1, column=0, padx=5, pady=5)
entry_seccion = tk.Entry(frame_academico)
entry_seccion.grid(row=1, column=1, padx=5, pady=5)

# Radiobuttons para el estado de inscripción
Var_estado_inscripcion = tk.StringVar()
label_estado_inscripcion = tk.Label(frame_estado_inscripcion, text="Estado de Inscripción:", bg= "blue")
label_estado_inscripcion.grid(row=0, column=0, padx=5, pady=5)
radio_inscrito = tk.Radiobutton(frame_estado_inscripcion, text="Inscrito", variable=Var_estado_inscripcion, value="Inscrito")
radio_inscrito.grid(row=0, column=1, padx=5, pady=5)
radio_no_inscrito = tk.Radiobutton(frame_estado_inscripcion, text="No Inscrito", variable=Var_estado_inscripcion, value="No Inscrito")
radio_no_inscrito.grid(row=0, column=2, padx=5, pady=5)

# Checkbuttons para las materias optativas
var_ingles = tk.IntVar()
var_historia = tk.IntVar()
var_fisica = tk.IntVar()
label_optativas = tk.Label(frame_optativas, text="Materia Optativas:")
label_optativas.grid(row=0, column=0, padx=5, pady=5)
check_ingles = tk.Checkbutton(frame_optativas, text="Inglés", variable=var_ingles)
check_ingles.grid(row=0, column=1, padx=5, pady=5)
check_historia = tk.Checkbutton(frame_optativas, text="Historia", variable=var_historia)
check_historia.grid(row=0, column=2, padx=5, pady=5)
check_fisica = tk.Checkbutton(frame_optativas, text="Física", variable=var_fisica)
check_fisica.grid(row=0, column=3, padx=5, pady=5)

# Comentarios Adicionales
label_comentarios = tk.Label(frame_comentarios, text="Comentarios")
label_comentarios.grid(row=0, column=0, padx=5, pady=5)
text_comentarios = tk.Text(frame_comentarios, height=4, width=30)
text_comentarios.grid(row=0, column=1, padx=5, pady=5)

# Menú desplegable para nivel escolar
label_nivel_escolar = tk.Label(frame_estudiante, text="Nivel Escolar")
label_nivel_escolar.grid(row=3, column=0, padx=5, pady=5)
nivel_escolar = ["Primaria", "Secundaria"]
var_nivel_escolar = tk.StringVar()
var_nivel_escolar.set(nivel_escolar[0])
menu_nivel_escolar = tk.OptionMenu(frame_estudiante, var_nivel_escolar, *nivel_escolar)
menu_nivel_escolar.grid(row=3, column=1, padx=5, pady=5)

#Botones de acción
btn_registrar = tk.Button(ventana, text="Registrar Estudiante", command=registro_estudiantes)
btn_registrar.pack(pady=10)
btn_limpiar = tk.Button(ventana, text="Limpiar Formulario", command=limpiar_formulario)
btn_limpiar.pack(pady=10)

#Ejecutar la aplicación
ventana.mainloop()