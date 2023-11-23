import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routes.hello import router as hello_router
from app.routes.categorias import router as categorias_router

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

# Después de inicializar la app con FastAPI()
app.include_router(categorias_router)