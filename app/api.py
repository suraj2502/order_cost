from fastapi import FastAPI, Body
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.routes.order import order_router
import os



# from app.database.create_admin_user import create_admin

app = FastAPI()

app.mount("/app", StaticFiles(directory="app"), name="app") #for serving static files
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    order_router,
    tags=["order_items"],
    prefix="/order_items",
)