from sqlalchemy import Column, Integer, String, Float

from app.database.database import Base

# Define the Product model, which represents the structure of the "products" table in the database.
# The Product model inherits from the Base class, which is a declarative base class provided by SQLAlchemy.
class Product(Base):

    __tablename__ = "products"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    description = Column(
        String
    )

    price = Column(
        Float,
        nullable=False
    )

    quantity = Column(
        Integer,
        default=0
    )