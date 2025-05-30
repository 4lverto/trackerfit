# ejercicios/flexion.py
# -------------------------------
# Requierements
# -------------------------------
from trackerfit.ejercicios.base import Ejercicio

# -------------------------------
# Helpers
# -------------------------------

class Flexion(Ejercicio):
    """
    Implementación del ejercicio 'Flexiones de Pecho'.
    Calcula el ángulo entre hombro, codo y muñeca para detectar la bajada completa del cuerpo.
    """
    def __init__(self, lado="derecho"):
            if lado=='derecho':
                puntos = (12,14,16) # Hombro (der) = 12 , Codo (der) = 14 y Muñeca (der) = 16
            else:
                puntos = (11,13,15) # Hombro (izq) = 11 , Codo (izq) = 13 y Muñeca (izq) = 15

            super().__init__(angulo_min=70,angulo_max=160,puntos=puntos)
            self.umbral_validacion = self.angulo_min