import easyocr
import sys
import os

# Crear el lector con el idioma español e inglés
lector = easyocr.Reader(['es', 'en'])

# Función para leer texto de una imagen
def leer_texto(ruta_imagen):
    if not os.path.exists(ruta_imagen):
        print("❌ La imagen no existe en la ruta especificada.")
        return

    resultados = lector.readtext(ruta_imagen)

    if not resultados:
        print("❗ No se detectó texto en la imagen.")
        return

    print("\n📜 Texto detectado:\n")
    for _, texto, _ in resultados:
        print(texto)

# Uso desde línea de comandos
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️ Por favor proporciona la ruta de la imagen. Ejemplo:\npython extraer_texto.py imagen.png")
    else:
        leer_texto(sys.argv[1])
