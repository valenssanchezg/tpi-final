from Modelo.CambioDeEstado import CambioDeEstado
from Modelo.Cliente import Cliente
from Modelo.Encuesta import Encuesta
from Modelo.Estado import Estado
from Modelo.Llamada import Llamada
from Modelo.Pregunta import Pregunta
from Modelo.RespuestaDeCliente import RespuestaDeCliente
from Modelo.RespuestaPosible import RespuestaPosible
from datetime import date

##Este archivo fue creado para contener todos los datos necesarios y que el gestor pueda acceder a ellos
estadoIniciado = Estado("Iniciada")
estadoFinalizado = Estado("Finalizada")

cambioEstado1 = CambioDeEstado(estadoIniciado)
cambioEstado11 = CambioDeEstado(estadoIniciado)
cambioEstado2 = CambioDeEstado(estadoFinalizado)

cambioEstado2.setFechaHoraInicio(date(2023, 5, 31))
cambioEstado11.setFechaHoraInicio(date(2023, 5, 30))

cliente1 = Cliente("12345678", "Juan Perez", "123456789")
cliente2 = Cliente("87654321", "María González", "987654321")
cliente3 = Cliente("45678912", "Pedro Sanchez", "654321987")

llamada1 = Llamada(cambioEstado1, cliente1)
llamada2 = Llamada(cambioEstado1, cliente2)
llamada3 = Llamada(cambioEstado11, cliente3)

llamada1.setCambioDeEstado(cambioEstado2)
llamada2.setCambioDeEstado(cambioEstado2)
llamada3.setCambioDeEstado(cambioEstado2)

    # Crear instancias de la clase RespuestaDeCliente
respuesta1 = RespuestaPosible("Muy Insatisfactorio", 1)
respuesta2 = RespuestaPosible("Insatisfactorio", 2)
respuesta3 = RespuestaPosible("Masculino", 1)
respuesta4 = RespuestaPosible("Femenino", 2)
respuesta5 = RespuestaPosible("Prefiero no decirlo", 3)
respuesta6 = RespuestaPosible("Si", 1)
respuesta7 = RespuestaPosible("No", 2)
respuesta8 = RespuestaPosible("Satisfactorio", 3)
respuesta9 = RespuestaPosible("Muy bueno", 4)
respuesta10 = RespuestaPosible("Excelente", 5)

    # Crear una instancia de la clase Pregunta
pregunta1 = Pregunta("¿Que te parecio el servicio?", [respuesta1, respuesta2, respuesta8, respuesta9, respuesta10])
pregunta2 = Pregunta("¿Cuál es tu género?", [respuesta3, respuesta4, respuesta5])
pregunta3 = Pregunta("¿Te pudimos ayudar en lo que necesitabas?", [respuesta6, respuesta7])


    # Asignar pregunta a respuesta
respuesta1.setPreguntaAsociada(pregunta1)
respuesta2.setPreguntaAsociada(pregunta1)
respuesta8.setPreguntaAsociada(pregunta1)
respuesta9.setPreguntaAsociada(pregunta1)
respuesta10.setPreguntaAsociada(pregunta1)
respuesta3.setPreguntaAsociada(pregunta2)
respuesta4.setPreguntaAsociada(pregunta2)
respuesta5.setPreguntaAsociada(pregunta2)
respuesta6.setPreguntaAsociada(pregunta3)
respuesta7.setPreguntaAsociada(pregunta3)

    # Crear una instancia de la clase Encuesta
encuesta1 = Encuesta("Encuesta Sobre el Servicio 1", date(2023, 12, 31), [pregunta1, pregunta2])
encuesta2 = Encuesta("Encuesta Sobre el Servicio 2", date(2023, 12, 31), [pregunta2, pregunta3])


respuestaCliente1 = RespuestaDeCliente(respuesta9)
respuestaCliente11 = RespuestaDeCliente(respuesta3)
respuestaCliente2 = RespuestaDeCliente(respuesta4)
respuestaCliente21 = RespuestaDeCliente(respuesta6)
respuestaCliente3 = RespuestaDeCliente(respuesta8)
respuestaCliente31 = RespuestaDeCliente(respuesta3)

llamada1.setRespuestaDeCliente(respuestaCliente1)
llamada1.setRespuestaDeCliente(respuestaCliente11)
llamada2.setRespuestaDeCliente(respuestaCliente2)
llamada2.setRespuestaDeCliente(respuestaCliente21)
llamada3.setRespuestaDeCliente(respuestaCliente3)
llamada3.setRespuestaDeCliente(respuestaCliente31)

llamadaArray = [llamada1, llamada2, llamada3]

arrayEncuestas = [encuesta1, encuesta2]

