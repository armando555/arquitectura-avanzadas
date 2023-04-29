from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base import EntityMeta as Base

class Bicycle(Base):
    __tablename__ = 'bicycles'
    id = Column(Integer, primary_key = True, index=True)
    name = Column(String(50), nullable=False )
    latitude = Column(Float, nullable=False )
    longitude = Column(Float, nullable=False )
    
    def __repr__(self) -> str:
        return f"id: {self.id}, name:{self.name}, latitude:{self.latitude}, longitude:{self.longitude}"