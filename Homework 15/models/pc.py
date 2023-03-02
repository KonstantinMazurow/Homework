from sqlalchemy import Column, Integer, String, ForeignKey
from models.database import Base


class Pc(Base):
    __tablename__ = 'pcs'

    id = Column(Integer, primary_key=True, index=True)
    model_id = Column(Integer, ForeignKey("products.id"))
    speed = Column(Integer)
    ram = Column(Integer)
    hd = Column(Integer)
    cd = Column(String)
    price = Column(Integer)

    def __init__(self, model_id: int, speed: int, ram: int, hd: int, cd: str, price: int):

        self.model_id = model_id
        self.speed = speed
        self.ram = ram
        self.hd = hd
        self.cd = cd
        self.price = price
        
