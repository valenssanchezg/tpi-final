class Encuesta:
    def __init__(self, descripcion, fechaFinVigencia, pregunta):
        self.descripcion = descripcion
        self.fechaFinVigencia = fechaFinVigencia
        self.pregunta = pregunta

    def getDescripcionEncuesta(self):
        return self.descripcion

    def setDescripcion(self, valor):
        self.descripcion = valor

    def getFechaFinVigencia(self):
        return self.fechaFinVigencia

    def setFechaFinVigencia(self, valor):
        self.fechaFinVigencia = valor

    def getPregunta(self):
        return self.pregunta

    def setPregunta(self, valor):
        self.pregunta.append(valor)

    def esEncuestaConPreguntas(self, preguntas):

        for preg in self.pregunta:
            descripcion = preg.getDescripcion()

            if descripcion not in preguntas:
                return False

        return True

