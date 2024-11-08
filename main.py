from typing import Union
from fastapi import FastAPI # Framework FastAPI
from firebase import firebase # Conexion a Firebase
from pydantic import BaseModel

app = FastAPI()

# Configuracion de firebase
firebaseConfig = {
  "apiKey": "AIzaSyCT9nTIY1dUvwJguH2CSlT6LvcBK304mPY",
  "authDomain": "estacionamiento-miidt-2024.firebaseapp.com",
  "databaseURL": "https://estacionamiento-miidt-2024-default-rtdb.firebaseio.com",
  "projectId": "estacionamiento-miidt-2024",
  "storageBucket": "estacionamiento-miidt-2024.firebasestorage.app",
  "messagingSenderId": "455540450136",
  "appId": "1:455540450136:web:324c3814d1aeade1a3fb2d",
  "measurementId": "G-QCX53YCWXE"
}

# Conexion a la bd
firebase = firebase.FirebaseApplication(firebaseConfig["databaseURL"], None)

# Clase para definir el tipo de los valores
class Esp32(BaseModel):
    estado: str
    hora_entrada_unix: str 
    hora_entrada_legible: str
    id: str

# Obtener todos los datos
@app.get("/")
def read_root():
    return firebase.get("/esp32/item", "")

# Obtener un dato en especifico
#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
 #return {"item_id": item_id, "q": q}

@app.post("/items")
def add_item(item: Esp32):
    result = firebase.post("/esp32/item", {
        "estado": item.estado,
        "hora_entrada_unix": item.hora_entrada_unix,
        "hora_entrada_legible": item.hora_entrada_legible,
        "id": item.id
    })
    return result