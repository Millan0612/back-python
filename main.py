from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import List
import easyocr
import shutil
import os

app = FastAPI()

# --------------------------------------------------------------
@app.get("/")
def read_root():
    return {"mensaje": "¡Hola desde FastAPI!"}

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"saludo": f"Hola, {nombre}!"}

@app.post("/enviar/{dato}")
def recibir_dato(dato: str):
    return {"respuesta": f"Me has enviado: {dato}"}

class Persona(BaseModel):
    nombre: str
    cedula: str

@app.post("/registrar")
def registrar_persona(persona: Persona):
    return {
        "nombre_recibido": persona.nombre,
        "cedula_recibida": persona.cedula
    }

# --------------------------------------------------------------
class Numeros(BaseModel):
    numeros: List[float]

@app.post("/numeros")
def procesar_numeros(data: Numeros):
    nums = data.numeros
    if len(nums) == 0:
        return {"error": "Debes enviar al menos un número."}
    return {
        "mayor": max(nums),
        "menor": min(nums),
        "promedio": sum(nums) / len(nums)
    }

# --------------------------------------------------------------
@app.post("/ocr")
async def leer_texto_desde_imagen(archivo: UploadFile = File(...)):
    # Guardar el archivo temporalmente
    ruta_temporal = f"temp_{archivo.filename}"
    with open(ruta_temporal, "wb") as buffer:
        shutil.copyfileobj(archivo.file, buffer)

    # Verificar que se haya guardado correctamente
    if not os.path.isfile(ruta_temporal):
        return {"error": "No se pudo guardar la imagen"}

    # Leer la imagen con EasyOCR
    lector = easyocr.Reader(['es'])  # Cambia 'es' por 'en' si tu texto está en inglés
    resultado = lector.readtext(ruta_temporal, detail=0)

    # Borrar la imagen temporal después de procesarla
    os.remove(ruta_temporal)

    return {"texto_detectado": resultado}
