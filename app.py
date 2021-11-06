from flask import Flask 

from db import create_db, seed_db 

app = Flask(__name__)

db = create_db(app)
conn = db.connect() 
cursor = conn.cursor() 

seed_db(cursor)

@app.route("/")
def index():
    return "Hello world!"