from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def get_docs_():
    return {"message": "congratulations!!You have retrived documents successfully"}

