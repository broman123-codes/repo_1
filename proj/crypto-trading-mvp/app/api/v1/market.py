from fastapi import APIRouter

router = APIRouter()

@router.get("/ticker")
def get_price():
    return {"symbol": "BTC/USDT", "price": 29800}

