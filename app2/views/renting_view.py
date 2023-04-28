from sqladmin import ModelView
from models.renting import Renting

class RentingAdmin(ModelView, model=Renting):
    column_list = [Renting.id, Renting.bicycle_id]