import openai
import os
from dotenv import load_dotenv
import agentops 
import random

load_dotenv()  # ✅ Load API key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")
agentops.init(AGENTOPS_API_KEY=os.getenv("AGENTOPS_API_KEY"))

# ✅ Mock Movie Seat Availability Data
MOVIE_DATABASE = {
    "New York": [
        {"name": "AMC Times Square", "movies": ["Dune: Part Two", "Deadpool 3", "Inside Out 2"], "seats": [50, 30, 10]},
        {"name": "Regal Union Square", "movies": ["Kung Fu Panda 4", "John Wick 4", "Avatar 3"], "seats": [20, 40, 5]}
    ],
    "Los Angeles": [
        {"name": "IMAX Hollywood", "movies": ["The Batman 2", "Doctor Strange 3", "Minions Rise"], "seats": [25, 15, 8]},
        {"name": "Cinemark LA", "movies": ["Frozen 3", "Black Panther 3", "Avengers 5"], "seats": [45, 10, 12]}
    ]
}

# ✅ Mock User Preferences Logging
USER_LOGS = []

def get_movie_recommendation(city: str, user_preferences: str):
    # ✅ Get the nearest theater (mock logic)
    theaters = MOVIE_DATABASE.get(city, [])
    if not theaters:
        return {"error": "No theaters found in this city"}

    best_theater = theaters[0]  # Select the first theater for now
    recommended_movies = best_theater["movies"]

    # ✅ Use OpenAI Agent to Personalize Movie Selection
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are an AI that recommends movies based on user preferences."},
            {"role": "user", "content": f"My preferences: {user_preferences}. Recommend the best movie."}
        ]
    )

    best_movie = response.choices[0].message.content.strip()

    # ✅ Mock Available Showtimes
    showtimes = ["2:00 PM", "5:00 PM", "8:30 PM"]
    available_seats = random.choice(best_theater["seats"])

    # ✅ Log User Queries
    USER_LOGS.append({"city": city, "preferences": user_preferences, "movie": best_movie})

    return {
        "city": city,
        "theater": best_theater["name"],
        "recommended_movie": best_movie,
        "showtimes": showtimes,
        "available_seats": available_seats
    }

agentops.end_session('Success')
