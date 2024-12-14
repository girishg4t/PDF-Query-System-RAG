from openai_api import generate_embeddings
from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from utils.pdf_utils import extract_text_from_pdf
from db.query_db import insert_pdf_data_into_db
router = APIRouter()


@router.post("/v1/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    API endpoint to upload a PDF and store its data in the database.
    :param file: Uploaded PDF file.
    :return: JSON response with success message.
    """
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400, detail="Only PDF files are allowed.")

    try:
        # Extract text from PDF
        text_pages = extract_text_from_pdf(file.file)
        if not text_pages:
            raise HTTPException(
                status_code=400, detail="No text extracted from PDF.")

        # Generate embeddings for the extracted text
        embeddings = generate_embeddings(text_pages)

        # Insert data into the database
        msg = insert_pdf_data_into_db(text_pages, embeddings)

        return JSONResponse(content={"message": msg}, status_code=200)

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error processing PDF: {e}")
