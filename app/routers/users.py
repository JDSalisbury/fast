from app.models import item, user
from fastapi import APIRouter

r = APIRouter()


@r.get("/{user_id}/items/{item_id}")
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


@r.post("/", response_model=user.UserOut)
async def create_user(*, user: user.UserIn):
    return user


@r.get("/me")
async def read_user_me():
    return {"username": "fakecurrentuser"}


@r.get("/{username}")
async def read_user(username: str):
    return {"username": username}
