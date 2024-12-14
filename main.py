from fastapi import FastAPI
from routers import upload_pdf, get_matches

app = FastAPI()

# Include routers
app.include_router(upload_pdf.router, tags=["PDF"])
app.include_router(get_matches.router, tags=["Matches"])


@app.get("/")
async def root():
    return {"message": "Welcome to the Vector Database API"}
