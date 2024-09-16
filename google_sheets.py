import os
import json
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SHEET_ID = os.getenv("SHEET_ID")
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")

creds = None

# Google Sheets API authentication
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)

def get_sheet_data(range_name):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_ID, range=range_name).execute()
    values = result.get('values', [])
    return values

def update_sheet_data(range_name, values):
    body = {'values': values}
    result = service.spreadsheets().values().update(
        spreadsheetId=SHEET_ID, range=range_name,
        valueInputOption='RAW', body=body).execute()
    return result
