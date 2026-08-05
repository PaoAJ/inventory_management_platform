from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate


class ProductRepository:

    def get_all(self, db: Session):
        return db.query(Product).all()


    def create(
        self,
        db: Session,
        product: ProductCreate
    ):
        db_product = Product(
            **product.model_dump()
        )

        db.add(db_product)

        db.commit()

        db.refresh(db_product)

        return db_product