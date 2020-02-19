from enum import Enum
from fastapi import FastAPI, Query
from models import item, user
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Somelthingalskdf lkasdf"}


@app.get("/test")
async def test():
    return {
        "message": "Test end point",
        "obj": {
            "id": 1,
            "name": "Jeff"
        }
    }


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


class SearchEngines(str, Enum):
    google = "google"
    bing = "bing"
    yahoo = "yahoo"


@app.get('/model/{search_engine}')
async def get_search(search_engine: SearchEngines):
    if search_engine.value == SearchEngines.google:
        return {"engine": 'www.google.com'}
    if search_engine.value == SearchEngines.bing:
        return {"engine": "www.bing.com"}
    if search_engine.value == SearchEngines.yahoo:
        return {"engine": "www.yahoo.com"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str = None):
#     ''' Optional Query Params, default and required... '''
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str = Query(None, max_length=50), short: bool = False):
    ''' Bool Type Example '''
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str = None, short: bool = False
):
    ''' Multiple Params '''
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.post("/items/")
async def create_item(item: item.Item):

    return item


@app.post("/user/", response_model=user.UserOut)
async def create_user(*, user: user.UserIn):
    return user
