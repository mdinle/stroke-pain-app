from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import Base, engine
from app.routers import auth
from app.routers.predict import router as predict_router

# DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
async def root():
    return {"message": "Welcome to the Stroke and Pain Prediction API."}

# Routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(predict_router, tags=["Prediction"])