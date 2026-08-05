from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.core.config import DATABASE_URL

# Create the database engine. This object acts as a central source of connections to a particular database, 
# providing both a factory as well as a holding space called a connection pool for these database connections. 
engine = create_engine(
    DATABASE_URL
)

# Create a configured "Session" class. This class will be used to create new Session objects that are bound to the engine.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create a base class for our models to inherit from. 
# This class will be used to define the structure of our database tables.
class Base(DeclarativeBase):
    pass