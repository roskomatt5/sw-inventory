from models import Contact, db
from app import app

def drop_table():
    with app.app_context():
        engine = db.get_engine(app=app)
        table_name = Contact.__contact__  # Get the table name from the Contact model

        with engine.connect() as connection:
            connection.execute(f"DROP TABLE IF EXISTS {table_name}")

if __name__ == "__main__":
    drop_table()
