from datetime import datetime


class RespuestaDeCliente:
    def __init__(self, respuestaSeleccionada):
        self.respuestaSeleccionada = respuestaSeleccionada
        self.fechaDeEncuesta = datetime.now()

    def getRespuestaSeleccionada(self):
        return self.respuestaSeleccionada

    def setRespuestaSeleccionada(self, valor):
        self.respuestaSeleccionada = valor

    def getFechaDeEncuesta(self):
        return self.fechaDeEncuesta

    def setFechaDeEncuesta(self, valor):
        self.fechaDeEncuesta = valor

    def getDescripcionRta(self):
        return self.respuestaSeleccionada.getDescripcionRta()

    def getDescPreguntaAsociada(self):
        return self.respuestaSeleccionada.getDescPreguntaAsociada()
