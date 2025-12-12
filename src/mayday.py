from typing import NamedTuple
from datetime import datetime, date, time

Vuelo = NamedTuple("Vuelo",     
    [("operador", str), # Compañía aérea que operaba el vuelo (opcional)
    ("codigo", str),   # Código de vuelo (opcional)
   ("ruta", str),     # Ruta del vuelo (opcional)
   ("modelo", str)])  # Modelo de avión que operaba el vuelo (opcional)

Desastre   = NamedTuple("Desastre",     
  [("fecha", date),                 # Fecha del desastre aéreo
    ("hora", time | None),        # Hora del desastre (opcional)  
    ("localizacion", str),        # Localización del desastre
    ("supervivientes",int),       # Supervivientes
    ("fallecidos",int),           # Fallecidos    
    ("fallecidos_en_tierra",int), # Fallecidos en tierra (no eran pasajeros del vuelo)
    ("operacion",str),        # Momento operativo del vuelo cuando ocurrió el desastre   
    ("vuelos", list[Vuelo])]) # Vuelos implicados en el desastre

def parsea_fecha(fecha:str) -> date:

  return datetime.strptime(fecha, "%D/%M/%Y")

if __name__ == "__main__":
  parsea_fecha("12/09/2007")