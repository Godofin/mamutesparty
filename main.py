# main.py
from fastapi import FastAPI
from models import Base
from database import engine
from routers import router  # Importe o roteador

# Cria as tabelas no banco de dados (caso ainda não existam)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Festas do Mamute")

app.include_router(router)




