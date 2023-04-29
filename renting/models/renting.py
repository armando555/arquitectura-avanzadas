from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.base import EntityMeta as Base
from datetime import datetime

class Renting(Base):
    __tablename__ = 'renting'
    id = Column(Integer, primary_key = True, index=True)
    bicycle_id = Column(Integer)
    date_in = Column(DateTime)
    date_out = Column(DateTime)
    
    def __repr__(self) -> str:
        return f"id: {self.id}, bicycle_id:{self.bicycle_id}, date_in:{self.date_in}, date_out:{self.date_out}"