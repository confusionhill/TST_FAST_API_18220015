from fastapi import APIRouter
from pydantic import BaseModel

mahasiswaRouter = APIRouter(
    prefix="/mahasiswa",
)

class Mahasiswa(BaseModel):
    nim: int
    name: str

@mahasiswaRouter.get("/")
async def getMahasiswa(nim: int = 0, nama: str = ""):
    dataMahasiswa = {
        "nim": nim,
        "nama": nama.replace('"',"")
    }
    return dataMahasiswa

@mahasiswaRouter.post("/")
async def postMahasiswa(mahasiswa: Mahasiswa):
    return mahasiswa