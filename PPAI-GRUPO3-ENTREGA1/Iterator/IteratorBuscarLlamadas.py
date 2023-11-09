from typing import List
from Modelo.Llamada import Llamada
from Iterator import IIterator

class IteratorBuscarLlamadas():
    
    elementoActual = None
    ##elementos:List[Llamada]

    def __init__(self, elementos):
        self.elementos = elementos
    
    def primero(self) -> None:
        self.elementoActual = 0

    
    def siguiente(self) -> None:
        self.elementoActual += 1

    
    def actual(self) -> Llamada:

        ##for llamada in range(self.actual, len(self.elementos)):
            ##if self.cumpleFiltro(llamada):
               ##return self.elementos[self.actual]
            ##else:
                ##return None
        
        ##return None
    
        if self.cumpleFiltro(self.elementos[self.elementoActual]):
               return self.elementos[self.elementoActual]
        else:
                return None

        ##if self.cumpleFiltro(self.elementos[self.actual]):
               ##return self.elementos[self.actual]
        ##else:
                ##self.actual += 1
                ##self.actual()




    
    def haTerminado(self) -> bool:
        if self.elementoActual >= len(self.elementos):
            return True
        else:
            return False

    
    
    def cumpleFiltro(self, llamada:Llamada) -> bool:
        return llamada.tieneRespuestas and llamada.esDePeriodo
            