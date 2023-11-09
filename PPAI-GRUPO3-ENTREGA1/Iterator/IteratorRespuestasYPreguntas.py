from typing import List
from Modelo.RespuestaDeCliente import RespuestaDeCliente
from Iterator import IIterator

class IteratorRespuestasYPreguntas():
    
    elementoActual: int
    elementos: List[RespuestaDeCliente]

    def __init__(self, elementos):
        self.elementos = elementos
    
    def primero(self) -> None:
        self.elementoActual = 0

    
    def siguiente(self) -> None:
        self.elementoActual += 1

    
    def actual(self) -> RespuestaDeCliente:
        return self.elementos[self.elementoActual]


    
    def haTerminado(self) -> bool:
        if self.elementoActual >= len(self.elementos):
            return True
        else:
            return False

    
    
    def cumpleFiltro(self, llamada:RespuestaDeCliente) -> bool:
        pass
            