# examples/video.py
# -------------------------------
# Requierements
# -------------------------------
from trackerfit import SessionManager, TipoEntrada

# -------------------------------
# Helpers
# -------------------------------

# Ruta relativa a un vídeo de prueba
video_path = "recursos/videos/curl_bicep/curl_bicep_1.mp4"

manager = SessionManager()
manager.iniciar_sesion(
    tipo=TipoEntrada.VIDEO,
    nombre_ejercicio="curl_bicep",
    fuente=video_path
)

# Espera a que se termine automáticamente
while manager.sesion_activa():
    pass

# Imprime resumen
reps = manager.obtener_repeticiones()
print(f"Repeticiones detectadas: {reps}")
print(manager.generar_resumen(reps))