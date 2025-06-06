# ejercicios/sentadilla.py
# -------------------------------
# Requierements
# -------------------------------
from trackerfit.ejercicios.base import Ejercicio

# -------------------------------
# Helpers
# -------------------------------

class Sentadilla(Ejercicio):
    """
    Implementación del ejercicio 'Sentadilla'.
    Calcula el ángulo entre cadera, rodilla y tobillo para contar repeticiones al descender completamente.
    """
    def __init__(self, lado="derecho"):
            if lado=='derecho':
                puntos = (24,26,28) # Cadera (der) = 24 , Rodilla (der) = 26 y Tobillo(der) = 28
            else:
                puntos = (23,25,27) # Cadera (der) = 23 , Rodilla (der) = 25 y Tobillo(der) = 27

            super().__init__(angulo_min=70,angulo_max=160,puntos=puntos)
            self.umbral_validacion = self.angulo_min