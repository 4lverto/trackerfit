# ejercicios/quad_entension.py
# -------------------------------
# Requierements
# -------------------------------
from trackerfit.ejercicios.base import Ejercicio

# -------------------------------
# Helpers
# -------------------------------

class QuadExtension(Ejercicio):
    """
    Implementación del ejercicio 'Extensión de Cuádriceps'.
    Calcula el ángulo entre cadera, rodilla y tobillo para detectar la extensión completa de la pierna.
    """
    def __init__(self , lado="derecho"):
        if(lado == "derecho"):
            puntos = (24,26,28) # Cadera (der) = 24, # Rodilla (der) = 26, Tobillo (der) = 28
        else:
            puntos = (23,25,27) # Cadera (izq) = 23, # Rodilla (izq) = 25, Tobillo (izq) = 27
            
        super().__init__(angulo_min=70,angulo_max=160,puntos=puntos)
        self.umbral_validacion = self.angulo_min