import csv
import sys
from typing import List

from Iterator import IIterator
from Iterator.IteratorBuscarLlamadas import IteratorBuscarLlamadas
from Iterator import IAgregado
from Modelo.Llamada import Llamada


class GestorConsultarEncuesta():
    fechaFin = None
    llamadaSeleccionada = None
    csvOImpresion = None
    csv = None
    nombreCliente = None
    estadoActual = None
    duracion = None
    respuestas = None
    preguntas = None
    encuesta = None
    descripcionEncuesta = None


    ## Esto lo modificamos para los iterator
    def crearIterador(self, elementos:List[Llamada]) -> IteratorBuscarLlamadas:
        iterator = IteratorBuscarLlamadas(elementos)
        return iterator

    def nuevaConsulta(self, pantalla, arrayLlamadas, arrayEncuestas, pantallaCsv):
        pantalla.pedirFechasDelPeriodoAFiltrar(self)
        llamadasFiltradas = self.buscarLlamadasDelPeriodo(arrayLlamadas)
        pantalla.mostrarLlamadasFiltradas(llamadasFiltradas, self)
        if len(llamadasFiltradas) > 0:
            pantalla.pedirSeleccionDeLlamada(llamadasFiltradas, self)
            self.buscarDatosDeLlamadaSeleccionada(self.llamadaSeleccionada, arrayEncuestas)
            pantalla.mostrarDatosDeLlamada(self.nombreCliente, self.estadoActual, self.duracion, self.respuestas, self.preguntas, self.descripcionEncuesta)
            pantalla.pedirSeleccionCsvOImpresion(self)
            if self.csvOImpresion == 1:
                archivoCsv = self.generarCSV()
                pantallaCsv.visualizarCsv(archivoCsv, self)

    def tomarFechasDelPeriodo(self, pantalla, fechaInicio, fechaFin):
        if self.validarFechas(fechaInicio, fechaFin):
            self.fechaInicio = fechaInicio
            self.fechaFin = fechaFin
        else:
            return False

    def validarFechas(self, fechaInicio, fechaFin):
        return fechaInicio <= fechaFin

    def buscarLlamadasDelPeriodo(self, llamadas):
        llamadasFiltradas = []
        iterator = self.crearIterador(llamadas)
        iterator.primero()
        ##for llamada in llamadas:
            ##if llamada.tieneRespuestas() and (llamada.esDePeriodo(self.fechaInicio, self.fechaFin)):
                ##llamadasFiltradas.append(llamada)
        while not iterator.haTerminado():
            llamada = iterator.actual()
            if llamada != None:
                llamadasFiltradas.append(llamada)
            iterator.siguiente()



        return llamadasFiltradas

    def tomarSeleccionDeLlamada(self, llamadaSelec):
        self.llamadaSeleccionada = llamadaSelec

    def buscarDatosDeLlamadaSeleccionada(self, llamada, encuestas):
        nombreCliente = llamada.getNombreClienteDeLlamada()
        estadoActual = llamada.obtenerEstadoActual()
        duracion = llamada.getDuracion()
        respuestas, preguntas = llamada.obtenerDescripcionDeRespuestasYPreguntas()
        encuesta = self.buscarEncuestaDeLlamada(preguntas, encuestas)
        descripcionEncuesta = encuesta.getDescripcionEncuesta()

        self.nombreCliente = nombreCliente
        self.estadoActual = estadoActual
        self.duracion = duracion
        self.respuestas = respuestas
        self.preguntas = preguntas
        self.encuesta = encuesta
        self.descripcionEncuesta = descripcionEncuesta

    def buscarEncuestaDeLlamada(self, preguntas, encuestas):
        for encuesta in encuestas:
            if encuesta.esEncuestaConPreguntas(preguntas):
                return encuesta

        return None

    def tomarSeleccionCsvOImpresion(self, codigo):
        self.csvOImpresion = codigo

    def generarCSV(self):
        archivoCsv = 'llamada.csv'

        with open(archivoCsv, 'w', newline='') as archivo:
            escritorCsv = csv.writer(archivo)

            escritorCsv.writerow(['Cliente', 'Estado de la llamada', 'Duración de la llamada'])

            escritorCsv.writerow([self.nombreCliente, self.estadoActual, self.duracion])

            escritorCsv.writerow([])

            for pregunta, respuesta in zip(self.preguntas, self.respuestas):
                escritorCsv.writerow([pregunta + ' || ', respuesta])

        return archivoCsv

    def cancelarCU(self, ventana):
        ventana.destroy()
        sys.exit()

    def finCU(self, ventana):
        ventana.destroy()
        sys.exit()



