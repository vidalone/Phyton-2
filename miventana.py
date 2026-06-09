import tkinter as tk


ventana = tk.Tk()

ventana.title("Hola ventana")
ventana.geometry("800x600")
etiqueta = tk.Label(ventana, text="Hola Juan",font="Arial 18 bold")
etiqueta.pack(pady=20)

boton = tk.Button(
    ventana,
    text="Clica aquí",
    command=lambda: etiqueta.config(text="Hola"),
    font=("Arial", 18),
    padx=20,
    pady=10,
)
boton.pack(pady=20)

ventana.mainloop()