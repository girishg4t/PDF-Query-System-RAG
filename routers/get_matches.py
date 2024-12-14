from openai_api import generate_embeddings_list
from fastapi import APIRouter, Query, Form, HTTPException
from fastapi.responses import JSONResponse
from db.query_db import get_matches
router = APIRouter()


@router.post("/v1/matches")
def get_matches_by_sentence(sentence: str = Form(...), limit: int = Form(...)):
    try:
        results = get_matches(sentence, limit)
        if not results:
            return JSONResponse(content={"message": "No matches found."}, status_code=200)

        # Format the results
        formatted_results = {"matches": [
            {"sentence": row[0], "distance": row[1]} for row in results]}
        return JSONResponse(content=formatted_results, status_code=200)

    except Exception as e:
        print(f"Error: {e}")
        return
