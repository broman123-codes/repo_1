from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def place_order():
    return {"status": "order placed"}

@router.get("/")
def list_orders():
    return [{"id": 1, "side": "buy", "amount": 0.5}]
