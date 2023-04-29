from sqladmin import ModelView
from models.bicycle import Bicycle

class BicycleAdmin(ModelView, model=Bicycle):
    column_list = [Bicycle.id, Bicycle.name]