
from pydantic import BaseModel, Field
from typing import Optional,List
from enum import Enum
from typing import Type




class order_items_schema(BaseModel):
    # class for order_items schema 
    name: str =Field(
        None, title="The name of the item", max_length=300,min_length=1
    )
    quantity: int = Field(...,gt=0,le=200)
    price:int=Field(...,gt=0,le=500000)


class status(str,Enum):
    FLAT = 'FLAT'
    DELIVERY = 'DELIVERY'
    
    
class offer_schema(BaseModel):
    offer_type:status
    offer_value:int=Field(...,ge=0)


class order_schema(BaseModel):
    order_items:List[order_items_schema]
    distance:int=Field(...,ge=0,le=500000)
    offer:Optional[offer_schema]=None
    
