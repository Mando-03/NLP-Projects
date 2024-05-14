from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from Recommend import recommend_product

app = FastAPI()


class RecommendationRequest(BaseModel):
    last_purchase_history: str


@app.post("/recommendations/")
async def get_recommendations(request: RecommendationRequest):
    try:
        # Predefined cluster number
        cluster_number = 4

        # Convert last_purchase_history from string to list
        history = request.last_purchase_history.split(',')

        # Call the recommend_product function
        recommendations = recommend_product(10, cluster_number, history)

        return {"recommendations": recommendations['recommendations']}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
