
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional,List
from enum import Enum
import inspect
from typing import Type

from fastapi import Form



class order_items_schema(BaseModel):
    # class for order_items schema 
    name: str =Field(
        None, title="The name of the item", max_length=300,min_length=1
    )
    quantity: int = Field(...,gt=0,le=1000)
    price:int=Field(...,gt=0,le=500000)


class status(str,Enum):
    FLAT = 'FLAT'
    DELIVERY = 'DELIVERY'
    
    
class offer_schema(BaseModel):
    offer_type:status
    offer_value:int=Field(...,ge=0)

class distance_schema(BaseModel):
    distance:int=Field(...,ge=0,le=500000)

class order_schema(BaseModel):
    order_items:List[order_items_schema]
    distance:int=Field(...,ge=0,le=500000)
    offer:Optional[offer_schema]=None
    
