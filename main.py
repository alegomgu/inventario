import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routes.hello import router as hello_router
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Incluir el router del endpoint Hello World
app.include_router(hello_router)

if __name__ == "__main__":
    # Aquí se podría incluir una función 'configure()' si es necesaria para configurar la app
    uvicorn.run(app, host="127.0.0.1", port=int("5000"))
