from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

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
