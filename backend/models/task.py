from pydantic import BaseModel

class Task(BaseModel):
    id: int
    name: str
    discription: str
    status: str
