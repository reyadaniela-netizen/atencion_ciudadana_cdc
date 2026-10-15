import os
from google import genai

# Inicializamos el cliente (automáticamente toma la API Key del entorno)
client = genai.Client()

def probar_prototipo():
    print("Enviando reporte de prueba a Gemma 4...")
    
    # Llamada al modelo ligero usando el ID exacto
    response = client.models.generate_content(
        model="gemma-4-26b-a4b-it",
        contents="Hay un bache enorme en la calle 31 de Ciudad del Carmen.",
        config={
            "system_instruction": "Eres un asistente de atención ciudadana para Ciudad del Carmen, Campeche. Analiza el reporte y responde clasificando: Categoría, Prioridad y Dependencia Responsable."
        }
    )
    
    print("\n--- RESPUESTA DE GEMMA 4 ---")
    print(response.text)

if __name__ == "__main__":
    probar_prototipo()