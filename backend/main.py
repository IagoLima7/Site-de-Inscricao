from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles 
from routers.form_router import router

app = FastAPI()

# Habilita CORS para permitir requisições do navegador (frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, substitua por ["http://seusite.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return {"mensagem": "API do Formulário está rodando!"}

# Inclui o roteador definido no seu controlador
app.include_router(router)
