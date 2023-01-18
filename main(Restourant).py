from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2


# create data schema
class Menu(BaseModel):  # menu serializer
    id: int
    name: str
    description: str
    price: float


def get_connection():
    connection = psycopg2.connect(
        host="host",
        port="port",
        user="user",
        password="password",
        database="database"
    )
    return connection


# app = FastAPI()


@app.get("/api/v1/menus")  # get data from page
async def read_menu():
    return {"Menu": 'menu'}


@app.post("/api/v1/menus")  # put data to page
async def post_menu(menu: Menu):
    return {menu: 'menu'}


@app.get("menu/{item_id}")
async def read_menu(item_id: int):
    return {
        # "id": menu.id,
        # "name": menu.name,
        # "description": menu.description,
        # "price": menu.price,
        "item": item_id
    }


@app.put("menu/{item_id}")
async def update_menu(item_id: int, menu: Menu):
    return {"id": menu.id,
            "name": menu.name,
            "description": menu.description,
            "price": menu.price,
            "item": item_id}


# @app.post("/menu/")
# async def create_menu_item(item: Menu):
#     connection = get_connection()
#     cursor = connection.cursor()
#
#     cursor.execute(f"INSERT INTO menu (name, description, price) VALUES ('{item.name}', '{item.description}', '{item.price}')")
#     connection.commit()
#     cursor.close()
#     connection.close()
#
#     return {"message": "Menu item has been created"}


# @app.get("/menu/{item_id}")
# async def read_menu_item(item_id: int):
#     connection = get_connection()
#     cursor = connection.cursor()
#
#     cursor.execute(f"SELECT * FROM menu WHERE id = {item_id}")
#     item = cursor.fetchone()
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     cursor.close()
#     connection.close()
#
#     return {"item": item}


# @app.put("/menu/{item_id}")
# async def update_menu_item(item_id: int, item: Menu):
#     connection = get_connection()
#     cursor = connection.cursor()
#
#     cursor.execute(f"UPDATE menu SET name='{item.name}', description='{item.description}',price='{item.price}' WHERE id = {item_id}")
#     connection.commit()
#     cursor.close()
#     connection.close()
#     return {"message": "Menu item has been updated"}
#
#
# @app.delete("/menu/{item_id}")
# async def delete_menu_item(item_id: int):
#     connection = get_connection()
#     cursor = connection.cursor()
#     cursor.execute(f"DELETE FROM menu WHERE id = {item_id}")
#     connection.commit()
#     cursor.close()
#     connection.close()
#
#     return {"message": "Menu item has been deleted"}
