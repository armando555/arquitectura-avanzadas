from typing import Optional
from pydantic import BaseModel


class BicycleBase(BaseModel):
    name: str
    longitude: float
    latitude: float
    
class BicycleSchema(BicycleBase):
    class Config():
        orm_mode = True
        
class ShowBicycleSchema(BicycleSchema):
    id: int

        

        