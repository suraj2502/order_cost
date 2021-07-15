from typing import List,Optional
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi import Query
from common_helper import ErrorResponseModel, ResponseModel
from fastapi import Request, Depends,Form
from app.model.order_model import order_items_schema,offer_schema,order_schema,status,distance_schema
from pydantic import BaseModel, Field
from enum import Enum

order_router = APIRouter()

def delivery_cost(distance):
            cost = 0
            if distance<=10000 :
                cost+= 5000
            elif distance<=20000:
                cost += 10000
            elif distance<= 50000:
                cost += 50000
            else:
                cost += 100000
            return cost


@order_router.post("/get_items_cost")
async def get_order_items_cost(request:Request,order_details:order_schema):

    total_cost=0 
    order_details=jsonable_encoder(order_details)
 
    for item in order_details["order_items"]:
        total_cost += item['quantity']*item['price']

    if order_details["offer"]!=None:
        if order_details["offer"]["offer_type"] == "FLAT":
            total_cost += delivery_cost(order_details["distance"])
            total_cost = max(total_cost - order_details["offer"]["offer_value"],0)
            
        elif order_details["offer"]["offer_type"] == "DELIVERY":
            pass
            
    else:
        total_cost += delivery_cost(order_details["distance"])
    
    response={'total_order_cost':total_cost }
    return ResponseModel(
        response,
        200,
        "cost calculated successfully.",
    )

"""
@order_router.post("/get_items_cost")
async def get_order_items_cost(request:Request,order_items:List[order_items_schema],distance_details:distance_schema,offer_details:Optional[offer_schema]=None):
#    if "error" in new_feed_data:
#        return ErrorResponseModel("An error occurred.", 409, "error")
    total_cost=0 
    print(order_items)
    print(offer_details)
    print(distance_details.distance)
    order_items=jsonable_encoder(order_items)
    print(order_items)
    for item in order_items:
        print(item["quantity"])
        total_cost += item['quantity']*item['price']

    if offer_details==None:
        return ResponseModel({'total_order_cost':total_cost},200,"cost calculated without any offer" )

    if offer_details.offer_type == "FLAT":
        total_cost += delivery_cost(distance_details.distance)

        total_cost = max(total_cost - offer_details.offer_value,0)
    elif offer_details.offer_type == "DELIVERY":
        pass
    else:
        total_cost += delivery_cost(distance_details.distance)

    response={'total_order_cost':total_cost }
    return ResponseModel(
        response,
        200,
        "cost calculated successfully.",
    )
"""
 