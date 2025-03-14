from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.plan import router as plan_router

app = FastAPI()

# ✅ Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include routes with the "/api" prefix
app.include_router(plan_router, prefix="/api")

@app.get("/")
def home():
    return {"message": "Plan Your Night API is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
