import json 

import flask 
from flask import Flask, request 

from db import create_db, seed_db 
from utils import build_data_dict, build_errors

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



"""
BOARD ENDPOINTS *************************************
"""

@app.route("/api/boards", methods=["GET"])
def get_boards():
    """ Returns all available boards """
    data_dict = build_data_dict(status="Success", status_code=200, data=True)

    with conn.cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM board")      
            cursor.fetchone()

            for record in cursor:
                data_dict["data"].append({
                    "id": record[0],
                    "name": record[1],
                    "description": record[2]
                })

        except Exception as e:
            data_dict = build_errors(data_dict, e)

    return flask.jsonify(data_dict)


@app.route("/api/boards/<id>", methods=["DELETE"])
def delete_board(id):
    """ Deletes a board """
    data_dict = build_data_dict(status=f"Deleted board {id}", status_code=202, data=False)
    cursor = conn.cursor() 

    try:
        cursor.execute("DELETE FROM board WHERE id=%s", (id))      
    except Exception as e:
        data_dict["statusCode"] = 500
        data_dict["status"] = f"Internal Server Error: {e}"

    return flask.jsonify(data_dict)


"""
SYMBOL ENDPOINTS *************************************
"""

@app.route("/api/symbol-types", methods=["GET"])
def get_symbol_types():
    """ Returns all available symbols types - gates, events, transfers"""
    data_dict = build_data_dict(status="Success", status_code=200, data=True)

    with conn.cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM symbol_type")      
            cursor.fetchone()

            for record in cursor:
                data_dict["data"].append({
                    "id": record[0],
                    "type": record[1]
                })

        except Exception as e:
            data_dict = build_errors(data_dict, e)

    return flask.jsonify(data_dict)


@app.route("/api/symbols", methods=["GET"])
def get_symbols():
    """ Returns all available symbols """
    data_dict = build_data_dict(status="Success", status_code=200, data=True)

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM symbol;")      
            cursor.fetchone()

            for record in cursor:
                data_dict["data"].append({
                    "id": record[0],
                    "name": record[1],
                    "description": record[2],
                    "type": record[3] 
                })

    except Exception as e:
            data_dict = build_errors(data_dict, e) 

    return flask.jsonify(data_dict)


@app.route("/api/symbols", methods=["POST"])
def create_symbols():
    """ Returns all available boards """
    data_dict = build_data_dict(status="Created", status_code=201, data=True) 

    try:
        # ensure required fields are present 
        data = request.json
        name = data["name"]
        description = data["description"]
        symbol_type = data["type"]

        with conn.cursor() as cursor: 
            cursor.execute(
                """INSERT INTO symbol(name, description, type) 
                   VALUES(%s, %s, %s)
                   RETURNING id
                """,
                (name, description, symbol_type)
            )

            new_row_id = cursor.fetchone()[0]
            cursor.execute("SELECT * FROM symbol WHERE id=%s", (new_row_id,))
            new_row = cursor.fetchone() 
            
            data_dict["data"].append({
                "id": new_row[0],
                "name": new_row[1],
                "description": new_row[2],
                "type": new_row[3] 
            })

    except Exception as e: 
        data_dict = build_errors(data_dict, e)

    return flask.jsonify(data_dict)


@app.route("/api/symbols/<id>", methods=["PUT","PATCH"])
def update_symbols(id):
    """ Returns all available boards """
    data_dict = build_data_dict(status="Updated successfully", status_code=204, data=True) 

    try:
        # ensure required fields are present 
        data = request.json
        name = data["name"]
        description = data["description"]
        symbol_type = data["type"]

        with conn.cursor() as cursor: 
            cursor.execute(
                """UPDATE symbol
                   SET name=%s, description=%s, type=%s
                   WHERE id=%s
                """,
                (name, description, symbol_type, id)
            )

            cursor.execute("SELECT * FROM symbol WHERE id=%s", (id,))
            udpated_row = cursor.fetchone() 
            
            data_dict["data"].append({
                "id": udpated_row[0],
                "name": udpated_row[1],
                "description": udpated_row[2],
                "type": udpated_row[3] 
            })

    except Exception as e: 
        data_dict = build_errors(data_dict, e)

    return flask.jsonify(data_dict)


@app.route("/api/symbols/<id>", methods=["DELETE"])
def delete_symbol(id):
    """ Deletes a board """
    data_dict = build_data_dict(status=f"Deleted symbol {id}", status_code=202, data=False)
    cursor = conn.cursor() 

    try:
        cursor.execute("DELETE FROM symbol WHERE id=%s", (id))      
    except Exception as e:
        data_dict["statusCode"] = 500
        data_dict["status"] = f"Internal Server Error: {e}"

    return flask.jsonify(data_dict)


if __name__ == "__main__":
    app.run()

