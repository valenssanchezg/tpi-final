import tkinter as tk
from datetime import datetime
from tkinter import ttk


class PantallaConsultarEncuesta:
    def __init__(self):
        self.ventana = tk.Tk()
        self.lblTitulo = tk.Label(self.ventana, text="IVR", font=("Cascadia Code Bold", 30), fg="#204561")
        self.lblSeleccionFechas = tk.Label(self.ventana, text="Seleccione las fechas", font=("Cascadia Code Semilight", 15))
        self.lblFechaInicio = tk.Label(self.ventana, text="Fecha inicio (dd/mm/aaaa):", font=("Candara", 12))
        self.lblFechaFin = tk.Label(self.ventana, text="Fecha fin (dd/mm/aa):", font=("Candara", 12))
        self.txtFechaInicio = tk.Entry(self.ventana)
        self.txtFechaFin = tk.Entry(self.ventana)
        self.btnAceptarFechasPeriodo = tk.Button(self.ventana, text="Aceptar", width=15, fg="white", bg="#E87B0E", font=("Cascadia Code", 12), relief="ridge")
        self.btnCancelar = tk.Button(self.ventana, text="Cancelar", width=15, font=("Cascadia Code", 12), bg="#E87B0E", fg="white", relief="ridge")
        self.lblLlamadasFiltradas = tk.Label(self.ventana, text="Llamadas del periodo seleccionado:", font=("Cascadia Code Semilight", 15))
        self.lblLamadas = tk.Label(self.ventana)
        self.lblSinLlamadas = tk.Label(self.ventana, text="No se encontraron llamadas del periodo", font=("Cascadia Code Semilight", 12))
        self.lblSeleccionLlamada = tk.Label(self.ventana, text="Seleccione una llamada:", font=("Cascadia Code Light", 12))
        self.cmbOpcionesLlamadas = ttk.Combobox(self.ventana, foreground="white", background="#204561", font=("Candara", 12))
        self.lblLlamadasNick = tk.Label(self.ventana)
        self.btnAceptarSeleccionLlamada = tk.Button(self.ventana, text="Aceptar", width=15, fg="white", bg="#E87B0E", font=("Cascadia Code", 12), relief="ridge")
        self.lblNombreCliente = tk.Label(self.ventana, font=("Candara", 12))
        self.lblEstadoActual = tk.Label(self.ventana, font=("Candara", 12))
        self.lblDuracion = tk.Label(self.ventana, font=("Candara", 12))
        self.lblDescripcionEncuesta = tk.Label(self.ventana, font=("Candara", 12))
        self.lblPreguntasYRespuestas = tk.Label(self.ventana, text="Preguntas y Respuestas ", font=("Candara", 12))
        self.lblPregunta = tk.Label(self.ventana)
        self.lblSeleccioneOpcionCsvOImpresion = tk.Label(self.ventana, text="Seleccione una opción:", font=("Cascadia Code Semilight", 12))
        self.cmbCsvOImpresion = ttk.Combobox(self.ventana, values=["Imprimir", "Generar CSV"], font=("Candara", 12))
        self.btnConfirmar = tk.Button(self.ventana, font=("Cascadia Code", 12), width=15, text="Confirmar", fg="white", bg="#E87B0E", relief="ridge")

    def opcionConsultarEncuesta(self, gestor, arrayLlamadas, arrayEncuestas, pantallaCsv):
        self.habilitarVentana()
        gestor.nuevaConsulta(self, arrayLlamadas, arrayEncuestas, pantallaCsv)
        # es parte del tkinter
        self.ventana.mainloop()

    def habilitarVentana(self):
        self.ventana.title("Mi Ventana")
        self.ventana.geometry("800x400")


    def pedirFechasDelPeriodoAFiltrar(self, gestor):
        self.lblTitulo.pack()
        self.lblSeleccionFechas.pack()
        self.lblFechaInicio.pack()
        self.txtFechaInicio.pack()
        self.lblFechaFin.pack()
        self.txtFechaFin.pack()

        btnAceptarClickeado = tk.Variable(self.ventana, value=False)

        btnAceptarFechasPeriodo = self.btnAceptarFechasPeriodo
        btnAceptarFechasPeriodo.config(command=lambda: btnAceptarClickeado.set(True))
        btnAceptarFechasPeriodo.place(x=330, y=200)

        btnCancelar = self.btnCancelar
        btnCancelar.config(command=lambda: btnAceptarClickeado.set(False))
        btnCancelar.place(x=550, y=300)

        self.ventana.wait_variable(btnAceptarClickeado)

        if btnAceptarClickeado.get():
            fechaInicio = self.tomarFechaInicioPeriodo(self.txtFechaInicio)
            fechaFin = self.tomarFechaFinPeriodo(self.txtFechaFin)
            gestor.tomarFechasDelPeriodo(self, fechaInicio, fechaFin)
        else:
            gestor.cancelarCU(self.ventana)

    def tomarFechaInicioPeriodo(self, fechaInicio):
        strFechaInicio = fechaInicio.get()
        datefechaInicio = datetime.strptime(strFechaInicio, "%d/%m/%Y").date()
        return datefechaInicio

    def tomarFechaFinPeriodo(self, fechaFin):
        strFechaFin = fechaFin.get()
        dateFechaFin = datetime.strptime(strFechaFin, "%d/%m/%Y").date()
        return dateFechaFin

    def mostrarLlamadasFiltradas(self, llamadas, gestor):
        widgetsDestruir = [self.lblSeleccionFechas, self.lblFechaInicio, self.lblFechaFin, self.txtFechaInicio, self.txtFechaFin, self.btnAceptarFechasPeriodo]
        for widget in self.ventana.winfo_children():
            if widget in widgetsDestruir:
                widget.destroy()

        contador = 0

        if len(llamadas) > 0:
            self.lblLlamadasFiltradas.pack()
            for llamada in llamadas:
                contador += 1
                lblLamadas = tk.Label(self.ventana, font=("Cascadia Code ExtraLight", 11))
                lblLamadas.config(text=str("Llamada " + str(contador)))
                lblLamadas.pack()
        else:
            self.lblSinLlamadas.place(x=250, y=150)
            btnCancelarClickeado = tk.Variable(self.ventana, value=False)

            btnCancelar = self.btnCancelar
            btnCancelar.config(command=lambda: btnCancelarClickeado.set(False))
            btnCancelar.place(x=550, y=300)

            self.ventana.wait_variable(btnCancelarClickeado)

            gestor.cancelarCU(self.ventana)

    def pedirSeleccionDeLlamada(self, llamadasFiltradas, gestor):

        self.lblSeleccionLlamada.pack()

        seleccion = tk.StringVar(self.ventana)
        seleccion.set("Seleccione Una Llamada")  # Establece el primer elemento como valor inicial

        lblLlamadasNick = [f"Llamada {i + 1}" for i in range(len(llamadasFiltradas))]

        cmbOpcionesLlamadas = self.cmbOpcionesLlamadas
        cmbOpcionesLlamadas['state'] = 'readonly'
        cmbOpcionesLlamadas.config(textvariable=seleccion, values=lblLlamadasNick)
        cmbOpcionesLlamadas.pack()

        btnSeleccionarLlamadaClickeado = tk.Variable(self.ventana, value=False)

        btnAceptarSeleccionLlamada = self.btnAceptarSeleccionLlamada
        btnAceptarSeleccionLlamada.config(command=lambda: btnSeleccionarLlamadaClickeado.set(True))
        btnAceptarSeleccionLlamada.pack()

        btnCancelar = self.btnCancelar
        btnCancelar.config(command=lambda: btnSeleccionarLlamadaClickeado.set(False))
        btnCancelar.place(x=550, y=300)

        self.ventana.wait_variable(btnSeleccionarLlamadaClickeado)

        if btnSeleccionarLlamadaClickeado.get():
            punteroLlamada = self.tomarSeleccionDeLlamada(llamadasFiltradas, seleccion)
            gestor.tomarSeleccionDeLlamada(punteroLlamada)
        else:
            gestor.cancelarCU(self.ventana)


    def tomarSeleccionDeLlamada(self, llamadasFiltradas, seleccion):
        llamadaSeleccionada = seleccion.get()
        contador = 0
        punteroLlamada = None
        for llamada in llamadasFiltradas:
            contador += 1
            if str(contador) in llamadaSeleccionada:
                punteroLlamada = llamada
        return punteroLlamada

    def mostrarDatosDeLlamada(self, nombreCliente, estadoActual, duracion, respuestas, preguntas, descripcionEncuesta):
        widgetsNoDestruir = [self.lblTitulo, self.lblNombreCliente, self.lblEstadoActual, self.lblDuracion, self.lblDescripcionEncuesta, self.btnCancelar,
                             self.lblPreguntasYRespuestas, self.lblPregunta, self.lblSeleccioneOpcionCsvOImpresion, self.cmbCsvOImpresion, self.btnConfirmar]

        for widget in self.ventana.winfo_children():
            if widget not in widgetsNoDestruir:
                widget.destroy()

        lblNombreCliente = self.lblNombreCliente
        lblNombreCliente.config(text="Nombre del cliente: " + nombreCliente)
        lblNombreCliente.pack()

        lblEstadoActual = self.lblEstadoActual
        lblEstadoActual.config(text="Estado actual: " + estadoActual)
        lblEstadoActual.pack()

        lblDuracion = self.lblDuracion
        lblDuracion.config(text="Duración: " + str(duracion) + " minutos")
        lblDuracion.pack()

        lblDescripcionEncuesta = self.lblDescripcionEncuesta
        lblDescripcionEncuesta.config(text="Descripción de la encuesta: " + descripcionEncuesta)
        lblDescripcionEncuesta.pack()

        self.lblPreguntasYRespuestas.pack()

        for pregunta, respuesta in zip(preguntas, respuestas):
            lblPregunta = tk.Label(self.ventana, text=pregunta + ": " + respuesta, font=("Candara", 12))
            lblPregunta.pack()

    def pedirSeleccionCsvOImpresion(self, gestor):

        self.lblSeleccioneOpcionCsvOImpresion.pack()

        cmbCsvOImpresion = self.cmbCsvOImpresion
        cmbCsvOImpresion['state'] = 'readonly'
        cmbCsvOImpresion.pack()

        btnConfirmarClickeado = tk.Variable(self.ventana, value=False)

        btnConfirmar = self.btnConfirmar
        btnConfirmar.config(command=lambda: btnConfirmarClickeado.set(True))
        btnConfirmar.place(x=100, y=300)

        btnCancelar = self.btnCancelar
        btnCancelar.config(command=lambda: btnConfirmarClickeado.set(False))
        btnCancelar.place(x=550, y=300)

        self.ventana.wait_variable(btnConfirmarClickeado)

        if btnConfirmarClickeado.get():
            codigo = self.tomarSeleccionCsvOImpresion(cmbCsvOImpresion.get())
            gestor.tomarSeleccionCsvOImpresion(codigo)
            self.ventana.destroy()
        else:
            gestor.cancelarCU(self.ventana)

    def tomarSeleccionCsvOImpresion(self, seleccion):
        if seleccion == "Imprimir":
            codigo = 2
        elif seleccion == "Generar CSV":
            codigo = 1
        else:
            codigo = 3
        return codigo
