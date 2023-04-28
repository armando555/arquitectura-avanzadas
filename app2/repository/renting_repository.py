from sqlalchemy.orm import Session
from models.renting import Renting
from schema.renting_schema import ShowRentingSchema, RentingSchema
from fastapi import status, HTTPException
from typing import List


def get_all(db: Session):
    rentings = db.query(Renting).all()
    return rentings


def create(request:RentingSchema, db: Session):
    new_renting = Renting(bicycle_id=request.bicycle_id, date_in=request.date_in, date_out=request.date_out)
    db.add(new_renting)
    db.commit()
    db.refresh(new_renting)
    return new_renting

def get(db: Session, id: int):
    renting = db.query(Renting).filter(Renting.id == id).first()
    if not renting:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'Renting with the id {id} is not available')
    return renting

def delete(db: Session, id: int):
    renting = db.query(Renting).filter(Renting.id == id)
    if not renting.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'Renting with the id {id} is not available')
    renting.delete(synchronize_session=False)
    db.commit()
    return "Renting deleted"

def update(db: Session, request: RentingSchema, id: int):
    renting = db.query(Renting).filter(Renting.id == id)
    if not renting.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'Renting with the id {id} is not available')
    renting.update(request.dict())
    db.commit()
    return "Updated"

def bulk(db: Session, request: List[RentingSchema]):
    for renting in request:
        new_renting= Renting(bicycle_id=renting.bicycle_id, date_in=renting.date_in, date_out=renting.date_out)
        db.add(new_renting)
    db.commit()
    return "Rentings created"