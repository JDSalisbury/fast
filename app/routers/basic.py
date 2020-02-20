from fastapi import APIRouter
from enum import Enum

r = APIRouter()


@r.get("/")
async def root():
    return {"message": "Somelthingalskdf lkasdf"}


@r.get("/test")
async def test():
    return {
        "message": "Test end point",
        "obj": {
            "id": 1,
            "name": "Jeff"
        }
    }


# @r.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


class SearchEngines(str, Enum):
    google = "google"
    bing = "bing"
    yahoo = "yahoo"


@r.get('/model/{search_engine}')
async def get_search(search_engine: SearchEngines):
    if search_engine.value == SearchEngines.google:
        return {"engine": 'www.google.com'}
    if search_engine.value == SearchEngines.bing:
        return {"engine": "www.bing.com"}
    if search_engine.value == SearchEngines.yahoo:
        return {"engine": "www.yahoo.com"}
