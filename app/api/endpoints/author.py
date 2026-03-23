from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_author():
    return{"message":"List author create success"}
