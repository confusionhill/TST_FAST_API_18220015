from fastapi import APIRouter, HTTPException

from models.mahasiswa import Mahasiswa

mahasiswaRouter = APIRouter(
    prefix="/mahasiswa",
)

@mahasiswaRouter.get("/")
async def getMahasiswa(nim: int, nama: str):
    if nim < 10000000 or nim > 19999999:
        raise HTTPException(status_code=404, detail="NIM is not available")
    dataMahasiswa = {
        "nim": nim,
        "nama": nama.replace('"',"")
    }
    return dataMahasiswa

@mahasiswaRouter.post("/")
async def postMahasiswa(mahasiswa: Mahasiswa):
    if ((mahasiswa.nim < 10000000) or (mahasiswa.nim > 19999999) ):
        raise HTTPException(status_code=404, detail="NIM is not available")
    return mahasiswa