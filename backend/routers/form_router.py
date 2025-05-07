from fastapi import APIRouter, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from urllib.parse import urlencode

router = APIRouter()

class Formulario(BaseModel):
    nome: str
    email: str
    telefone: str
    data_nascimento: str

templates = Jinja2Templates(directory="templates")

@router.post("/enviar")
def receber_dados(dados: Formulario):
    params = {
        "nome": dados.nome,
        "email": dados.email,
        "telefone": dados.telefone,
        "data_nascimento": dados.data_nascimento
    }
    query_string = urlencode(params)
    return RedirectResponse(url=f"/sucesso?{query_string}", status_code=302)

@router.get("/sucesso", response_class=HTMLResponse)
def sucesso(request: Request, nome: str, email: str, telefone: str, data_nascimento: str):
    return templates.TemplateResponse("sucesso.html", {
        "request": request,
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "data_nascimento": data_nascimento
    })
