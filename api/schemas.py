from pydantic import BaseModel
from typing import List 

class FoodItem(BaseModel):
    ean: str
    name: str
    carbohydrates_g: float 
    fats_g: float
    proteins_g: float

class SelectedElement(FoodItem):
    number: int 

class MenuRequest(BaseModel):
    elements: List[SelectedElement] 
    language: str