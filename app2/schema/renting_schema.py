from typing import Optional
from pydantic import BaseModel
from datetime import datetime



class RentingBase(BaseModel):
    bicycle_id: int
    date_in: datetime
    date_out: datetime
    
class RentingSchema(RentingBase):
    class Config():
        orm_mode = True
        
class ShowRentingSchema(RentingSchema):
    id: int

        

        