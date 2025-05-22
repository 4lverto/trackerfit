# examples/usar_camara.py
# -------------------------------
# Requierements
# -------------------------------
from trackerfit import SessionManager, TipoEntrada

# -------------------------------
# Helpers
# -------------------------------

# Inicia una sesión desde cámara con el ejercicio de curl de bíceps
manager = SessionManager()
manager.iniciar_sesion(
    tipo=TipoEntrada.CAMARA,
    nombre_ejercicio="curl_bicep"
)

# Espera a que se finalice manualmente
while manager.sesion_activa():
    pass

# Muestra el resumen
reps = manager.obtener_repeticiones()
print(f"Repeticiones detectadas: {reps}")
print(manager.generar_resumen(reps))
