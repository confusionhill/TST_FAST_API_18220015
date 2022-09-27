from fastapi import APIRouter

from models.mahasiswa import Mahasiswa

mahasiswaRouter = APIRouter(
    prefix="/mahasiswa",
)

@mahasiswaRouter.get("/")
async def getMahasiswa(nim: int, nama: str):
    dataMahasiswa = {
        "nim": nim,
        "nama": nama.replace('"',"")
    }
    return dataMahasiswa

@mahasiswaRouter.post("/")
async def postMahasiswa(mahasiswa: Mahasiswa):
    return mahasiswa