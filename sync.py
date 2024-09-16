from sqlalchemy.orm import Session
from database import Player
import google_sheets

# Synchronize from Google Sheets to MySQL
def sync_google_sheet_to_db(db: Session):
    # Updated range to include ID column
    data = google_sheets.get_sheet_data('Sheet1!A2:D')
    
    for row in data:
        id, name, age, role = row[0], row[1], int(row[2]), row[3]
        # Fetch the player by ID
        player = db.query(Player).filter(Player.id == id).first()
        if player:
            player.name = name
            player.age = age
            player.role = role
        else:
            player = Player(id=id, name=name, age=age, role=role)
            db.add(player)
        db.commit()

# Synchronize from MySQL to Google Sheets
def sync_db_to_google_sheet(db: Session):
    players = db.query(Player).all()
    # Include ID in the data to match the Google Sheets structure
    sheet_data = [[p.id, p.name, p.age, p.role] for p in players]
    # Updated range to include ID column
    google_sheets.update_sheet_data('Sheet1!A2:D', sheet_data)
