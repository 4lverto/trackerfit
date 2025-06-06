# core/ejercicios/elevacion_lateral.py
# -------------------------------
# Requierements
# -------------------------------
from trackerfit.ejercicios.base import Ejercicio

# -------------------------------
# Helpers
# -------------------------------

class ElevacionLateral(Ejercicio):
    """
    Implementación del ejercicio 'Elevación Lateral de Hombros'.
    Calcula el ángulo entre muñeca, hombro y cadera para contar repeticiones de subida de brazo.
    """
    def __init__(self, lado="derecho"):
            if lado=='derecho':
                puntos = (16,12,24) # Muñeca (der) = 16 , Hombro (der) = 12 y Cadera (der) = 24
            else:
                puntos = (15,11,23) # Muñeca (izq) = 15 , Hombro (izq) = 11 y Cadera (izq) = 23

            super().__init__(angulo_min=40,angulo_max=90,puntos=puntos)
            self.umbral_validacion = self.angulo_min