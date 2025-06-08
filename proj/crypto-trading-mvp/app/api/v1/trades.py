from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_trades():
    return [{"id": 1, "price": 30000, "amount": 0.1}]

