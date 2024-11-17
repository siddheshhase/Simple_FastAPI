from fastapi import FastAPI, APIRouter,status
import os
import json
from pydantic import BaseModel

router = APIRouter()

file_name = '/D/SiddhU_Task/API/database.json'

class DataModel(BaseModel):
    id: int 
    name: str
    email: str | None = None


@router.get("/users", status_code=status.HTTP_200_OK)
def get_users():
    data = None
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
    return data

@router.post("/users", status_code=status.HTTP_201_CREATED)
async def insert_user(payload: DataModel):

    with open(file_name, 'w') as json_file:
        json.dump(payload, json_file, indent=4)
        return {"Data is stored"}
