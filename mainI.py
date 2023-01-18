import fastapi
import sqlalchemy
import sqlalchemy.orm
from pydantic import BaseModel

# app = fastapi.FastAPI()

# DATABASE_URL = "postgresql://user:password@localhost:5432/database"
#
# engine = sqlalchemy.create_engine(DATABASE_URL)
#
#
# def get_db():
#     try:
#         db = sqlalchemy.orm.SessionLocal()
#         yield db
#     finally:
#         db.close()
#
#
# @app.get("/users/{user_id}")
# async def read_user(user_id: int, db: sqlalchemy.orm.Session = fastapi.Depends(get_db)):
#     user = db.execute("SELECT * FROM users WHERE id = :id", {"id": user_id}).fetchone()
#     return user


# create data schema
class Menu(BaseModel):  # menu serializer
    id: int
    name: str
    description: str
    price: float


@app.get("")
def main():
    return {"Main page": "Success"}


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

