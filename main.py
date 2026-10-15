import os
from google import genai

# Inicializamos el cliente (toma la API key de la variable de entorno)
client = genai.Client()

def iniciar_atencion_ciudadana():
    print("==================================================")
    print("  MUNICIPIO DE CARMEN - ASISTENTE DE ATENCIÓN CÍVICA")
    print("  Modelo: Gemma (gemma-4-26b-a4b-it)")
    print("==================================================")
    print("Escribe tu reporte o queja (escribe 'salir' para terminar):\n")

    # System instruction para guiar el comportamiento oficial del modelo
    system_prompt = (
        "Eres un asistente oficial de atención ciudadana para el municipio de "
        "Ciudad del Carmen, Campeche. Analiza el reporte del ciudadano y responde "
        "de forma profesional clasificando los siguientes puntos:\n"
        "1. Categoría (ej. Obras Públicas, Servicios Públicos, Agua Potable, Protección Civil)\n"
        "2. Prioridad (Baja, Media, Alta, Urgente)\n"
        "3. Dependencia Responsable\n"
        "4. Breve recomendación de acción o folio simulado."
    )

    while True:
        # Entrada interactiva del usuario
        reporte_usuario = input("\nCiudadano/a > ")
        
        if reporte_usuario.lower() in ["salir", "exit", "quit"]:
            print("\n¡Gracias por usar el prototipo de atención ciudadana! Saliendo...")
            break
            
        if not reporte_usuario.strip():
            print("Por favor, ingresa un reporte válido.")
            continue

        print("\nProcesando reporte con Gemma...")

        try:
            # Llamada al modelo con la entrada dinámica
            response = client.models.generate_content(
                model="gemma-4-26b-a4b-it",
                contents=reporte_usuario,
                config={
                    "system_instruction": system_prompt
                }
            )
            
            print("\n--- RESPUESTA OFICIAL DEL SISTEMA ---")
            print(response.text)
            print("-------------------------------------")

        except Exception as e:
            print(f"\n[Error de conexión con el modelo]: {e}")

if __name__ == "__main__":
    iniciar_atencion_ciudadana()