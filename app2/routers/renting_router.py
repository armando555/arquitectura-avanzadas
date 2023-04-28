from fastapi import APIRouter, Depends, status
from typing import List
from schema.renting_schema import ShowRentingSchema,RentingSchema
from sqlalchemy.orm import Session
from database.engine import get_db_connection
from repository import renting_repository


router = APIRouter(
    prefix="/rentings",
    tags=["Renting"]
)

@router.post("/",status_code=status.HTTP_201_CREATED)
async def create(request: RentingSchema, db: Session = Depends(get_db_connection)):
    return renting_repository.create(request, db)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ShowRentingSchema])
async def all(db: Session = Depends(get_db_connection)):
    return renting_repository.get_all(db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ShowRentingSchema)
async def get(id, db: Session = Depends(get_db_connection)):
    return renting_repository.get(db, id)

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete(id,db: Session = Depends(get_db_connection)):
    return renting_repository.delete(db, id)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update(id, request: ShowRentingSchema, db: Session = Depends(get_db_connection)):
    return renting_repository.update(db, request, id)

@router.post("/rentings", status_code=status.HTTP_200_OK)
async def bulk(request: List[ShowRentingSchema], db: Session = Depends(get_db_connection)):
    return renting_repository.bulk(db=db, request=request)

