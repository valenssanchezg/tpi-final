from abc import ABC, abstractmethod
from Modelo import Llamada

class IIterator(ABC):

    @abstractmethod
    def primero(self) -> None:
        pass

    @abstractmethod
    def siguiente(self) -> None:
        pass

    @abstractmethod
    def actual(self) -> Llamada:
        pass

    @abstractmethod
    def haTerminado(self) -> bool:
        pass
    
    @abstractmethod
    def cumpleFiltro(self, llamadas:Llamada) -> bool:
        pass

