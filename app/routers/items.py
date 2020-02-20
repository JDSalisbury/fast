from fastapi import APIRouter, Query
from app.models import item
r = APIRouter()


@r.get("/items/{item_id}")
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


@r.post("/items/")
async def create_item(item: item.Item):

    return item


# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str = None):
#     ''' Optional Query Params, default and required... '''
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}
