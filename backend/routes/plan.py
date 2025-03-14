from fastapi import APIRouter, Request, HTTPException
from services.ai_agent import get_movie_recommendation

router = APIRouter()

@router.post("/plan")
async def generate_plan(request: Request):
    try:
        body = await request.json()
        city = body.get("city")
        preferences = body.get("preferences", "action movies")  # Default to action movies if not provided

        if not city:
            raise HTTPException(status_code=400, detail="City name is required")

        plan = get_movie_recommendation(city, preferences)
        return plan
    except Exception as e:
        return {"error": str(e)}
