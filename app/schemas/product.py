from pydantic import BaseModel, Field

# Define Pydantic models for product creation, update, and response.

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: str | None = None
    price: float = Field(..., gt=0)
    quantity: int = Field(default=0, ge=0)


class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = Field(default=None, gt=0)
    quantity: int | None = Field(default=None, ge=0)


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    price: float
    quantity: int

    model_config = {
        "from_attributes": True
    }