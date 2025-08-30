from sqlalchemy import Column, Integer, String


from .base import Base


class Phones(Base):
    __tablename__ = "phones"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=True)
    phone = Column(Integer, nullable=True)
