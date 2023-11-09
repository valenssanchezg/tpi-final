from datetime import date


class CambioDeEstado:
    def __init__(self, estado):
        self.fechaHoraInicio = date.today()
        self.estado = estado

    def getFechaHoraInicio(self):
        return self.fechaHoraInicio

    def setFechaHoraInicio(self, valor):
        self.fechaHoraInicio = valor

    def getEstado(self):
        return self.estado

    def setEstado(self, valor):
        self.estado = valor

    def getNombreEstado(self):
        return self.estado.getNombre()
