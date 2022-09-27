from fastapi import FastAPI
from modules.mahasiswa.mahasiswaController import mahasiswaRouter

app = FastAPI()
app.include_router(mahasiswaRouter)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
