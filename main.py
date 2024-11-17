from fastapi import FastAPI
import uvicorn
from API import task_api

app = FastAPI()


app.include_router(task_api.router, tags=["Task API's"])

@app.get("/")
async def application_root():
    return {"Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host='127.0.0.1', reload=True)