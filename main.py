from fastapi import FastAPI

app = FastAPI(
    title="MotoPeças API",
    description="API para gerenciamento de peças de motocicletas",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "mensagem": "MotoPeças API funcionando!"
    }
