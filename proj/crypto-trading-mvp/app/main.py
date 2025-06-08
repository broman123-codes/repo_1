
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import auth, trades, orders, market, users

app = FastAPI(
    title="Crypto Trading MVP",
    version="0.1.0",
    description="A minimal crypto trading platform MVP built with FastAPI.",
)

# CORS settings for frontend
origins = [
    "http://localhost:3000",  # Next.js dev URL
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(orders.router, prefix="/api/v1/orders", tags=["orders"])
app.include_router(trades.router, prefix="/api/v1/trades", tags=["trades"])
app.include_router(market.router, prefix="/api/v1/market", tags=["market"])

# Health check
@app.get("/")
def read_root():
    return {"status": "ok", "message": "Crypto Trading API is running"}
