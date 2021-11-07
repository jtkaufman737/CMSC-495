from flask import Flask 

from db import create_db, seed_db 

app = Flask(__name__)

db = create_db(app)
conn = db.connect() 

seed_db(conn)


@app.route("/")
def index():
    return "Hello world!"