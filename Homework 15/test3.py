'''    
    Найдите номер модели, скорость и размер жесткого диска ПК, 
    имеющих 12х или 24х CD и цену менее 600 долларов.
'''

from models.database import engine
from sqlalchemy.orm import Session
from models.pc import Pc
from models.product import Product
from sqlalchemy import or_

def get_query3(speed_cd1, speed_cd2, value):
    with Session(autoflush=False, bind=engine) as db:
        result = db.query(
            Pc.speed, 
            Pc.hd, 
            Product.manufacturer,
            Product.model
            ).join(
            Product,
            Product.id == Pc.model_id,
            isouter = True
            ).filter(
            or_(Pc.cd == speed_cd1, Pc.cd == speed_cd2), 
            Pc.price < value).all()
            
        for u in result:
            print(f'Manufacturer: {u.manufacturer} Model: {u.model} Speed: {u.speed} HDD: {u.hd}')


