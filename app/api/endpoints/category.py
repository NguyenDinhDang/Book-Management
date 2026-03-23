from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_category():
    return{"message":"List category create success"}
