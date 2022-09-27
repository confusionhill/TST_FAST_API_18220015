from pydantic import BaseModel
class Mahasiswa(BaseModel):
    nim: int
    name: str