from fastapi import FastAPI
from app.validation import router as validation_router
from app.returns import router as returns_router
from app.performance import router as performance_router

app = FastAPI(title="BlackRock Challenge API")

app.include_router(validation_router)
app.include_router(returns_router)
app.include_router(performance_router)

@app.get("/")
def root():
    return {"message": "BlackRock Challenge API running"}