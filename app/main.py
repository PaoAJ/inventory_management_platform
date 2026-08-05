from fastapi import FastAPI

from app.database.database import engine, Base
from app.models import product
from app.api.routes import products


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Inventory Management API"
)


@app.get("/")
def root():
    return {
        "message": "Inventory Management API"
    }

app.include_router(products.router)