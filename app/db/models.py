from geoalchemy2 import Geography
from sqlalchemy import Column, Integer, Float

from .database import Base


class Apartments(Base):
    __tablename__ = "apartments"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    geopos = Column(Geography('POINT'), nullable=False)
    apartments = Column(Integer)
    price = Column(Float)
    year = Column(Integer)
