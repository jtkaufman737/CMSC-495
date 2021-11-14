import json 

import flask 
from flask import Flask 

from db import create_db, seed_db 

app = Flask(__name__)

db = create_db(app)
conn = db.connect() 

seed_db(conn)

"""
Endpoint structure

@app.route("/items", methods=["GET"])
def get_items(): 
    data_dict = {} 

    # we are going to use a "try/catch" to build error messages if something goes wrong 
    try:
        data = db.execute("SELECT * FROM items") 
        # will return a tuple, like ("item a", "blue")
        # from there, you need to use variables to turn the tuple into a dictionary 
        item_name, item_color = data 
        # will assign variable "item_name" to equal data[0], and variable "item_color" to equal data[1]
        # from there, you can build a python dictionary 

        data_dict["statusCode"] = 200
        data_dict["status] = "success"
        data_dict["item_name"] = item_name
        data_dict["item_color"] = item_color 
    
    except Exception as e:
        data_dict["statusCode"] = 500
        data_dict["status"] = f"Internal Server Error: {e}" # << fills in the error message

    return flask.jsonify(data_dict)

"""
@app.route("/boards/<id>", methods=["DELETE"])
def delete_board(id):
    data_dict = {} 
    cursor = conn.cursor() 

    try:
        cursor.execute("DELETE FROM board WHERE id=%s", (id))
        
        
        data_dict["statusCode"] = 202 
        data_dict["status"] = f"Deleted board {id}"
    except Exception as e:
        data_dict["statusCode"] = 500
        data_dict["status"] = f"Internal Server Error: {e}"
    
    cursor.close() 

    return flask.jsonify(data_dict)
