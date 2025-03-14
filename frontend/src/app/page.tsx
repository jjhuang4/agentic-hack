"use client";

import { useState } from "react";

// ✅ Define the expected structure of API response
interface MoviePlan {
  theater: string;
  recommended_movie: string;
  showtimes: string[];
  available_seats: number;
}

export default function Home() {
  const [city, setCity] = useState("");
  const [preferences, setPreferences] = useState("");
  const [result, setResult] = useState<MoviePlan | null>(null); // ✅ Added type for result

  const getPlan = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/plan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ city, preferences }),
      });

      if (!response.ok) {
        throw new Error("Failed to get plan");
      }

      const data: MoviePlan = await response.json(); // ✅ Ensure response matches the MoviePlan type
      setResult(data);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4">
      <h1 className="text-2xl font-bold text-black">Plan Your Movie Night</h1>

      <div className="w-full max-w-md p-4 bg-white rounded shadow-md">
        <input
          type="text"
          className="w-full p-2 border rounded text-black"
          placeholder="Enter City Name"
          value={city}
          onChange={(e) => setCity(e.target.value)}
        />
        <input
          type="text"
          className="w-full p-2 border rounded text-black mt-2"
          placeholder="Enter Movie Preferences (Optional)"
          value={preferences}
          onChange={(e) => setPreferences(e.target.value)}
        />
        <button
          className="w-full p-2 bg-blue-500 text-white rounded mt-2"
          onClick={getPlan}
        >
          Get Movie Plan
        </button>

        {result && (
          <div className="mt-4 p-4 bg-gray-100 rounded">
            <h2 className="text-lg font-bold text-black">Recommended Plan</h2>
            <p className="text-black"><strong>Theater:</strong> {result.theater}</p>
            <p className="text-black"><strong>Movie:</strong> {result.recommended_movie}</p>
            <p className="text-black"><strong>Showtimes:</strong> {result.showtimes?.join(", ") || "No showtimes available"}</p>
            <p className="text-black"><strong>Available Seats:</strong> {result.available_seats ?? "No seats available"}</p>
          </div>
        )}
      </div>
    </div>
  );
}
