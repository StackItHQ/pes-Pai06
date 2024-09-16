from fastapi import FastAPI, Depends
from database import get_db
from sync import sync_google_sheet_to_db, sync_db_to_google_sheet
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}

@app.get("/favicon.ico")
def favicon():
    return {"message": "No favicon available"}

@app.post("/sync/google-to-db")
def sync_google_to_db(db: Session = Depends(get_db)):
    sync_google_sheet_to_db(db)
    return {"status": "Google Sheets data synced to database"}

@app.post("/sync/db-to-google")
def sync_db_to_google(db: Session = Depends(get_db)):
    sync_db_to_google_sheet(db)
    return {"status": "Database data synced to Google Sheets"}
