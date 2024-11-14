# C:\Users\#####\AppData\Local\Programs\Python\Python313>python -m pip install pillow
# pip install fastapi
# pip install "fastapi[standard]"
# pip install uvicorn[standard]
# https://blog.postman.com/how-to-build-an-api-in-python/
# https://fastapi.tiangolo.com/deployment/manually/

from fastapi import FastAPI
from connect import mySQLCon

app = FastAPI()

# ENDPOINT localhost:8000/helloworld


@app.get("/helloworld")
async def read_root():
    return {"Message": "Saludos desde tu nueva API"}

# ENDPOINT http://127.0.0.1:8000/conParametros?name=HelloWorld


@app.get("/conParametros")
async def parametros(name: str):
    return {"Message": "Saludos " + name}

# Habría que hacer un Endpoint para cada parte del CRUD
# fastapi run ./7_API/api.py

# JUGAMOS UN POCO

# http://127.0.0.1:8000/insertamosUsuario?nombre=Hello&apellidos=World


@app.get("/insertamosUsuario")
async def insertUsuario(nombre: str = "Pepinillos", apellidos: str = "Frescos"):
    cone = mySQLCon()
    # cone.createTables()
    print(cone.createUser(nombre, apellidos))
    return {"Message": "Usuario: " + nombre + " con apellidos " + apellidos + ":CREADO"}
