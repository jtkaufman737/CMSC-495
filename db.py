from flask import Flask 
from flaskext.mysql import MySQL 

def create_db(app):
    app.config["MYSQL_DATABASE_USER"] = "root" 
    app.config["MYSQL_DATABASE_PASSWORD"] = "mysqluser" 
    app.config["MYSQL_DATABASE_DB"] = "fault_tree" 
    app.config["MYSQL_DATABASE_HOST"] = "localhost"  

    mysql = MySQL()
    mysql.init_app(app)
    return mysql 

def seed_db(conn):
    try:
        cursor = conn.cursor()
        # Split statements because for this middleware, cursor breaks on ";"
        statements = ['''
        CREATE TABLE IF NOT EXISTS board ( 
            id INTEGER NOT NULL AUTO_INCREMENT,  
            name VARCHAR(100),
            description VARCHAR(500),
            PRIMARY KEY(id)
        )''',
        '''
        CREATE TABLE IF NOT EXISTS symbol_type ( 
            id INTEGER NOT NULL AUTO_INCREMENT,  
            type VARCHAR(30),
            PRIMARY KEY(id)
        )''',
        '''
        CREATE TABLE IF NOT EXISTS symbol (
            id INTEGER NOT NULL AUTO_INCREMENT, 
            name VARCHAR(100),
            description VARCHAR(200),
            type INT,
            child_board INT,
            PRIMARY KEY(id),
            FOREIGN KEY(type) REFERENCES symbol_type(id) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY(child_board) REFERENCES board(id) ON DELETE CASCADE ON UPDATE CASCADE
        )''',
        '''
        CREATE TABLE IF NOT EXISTS board_symbol (
            board_id INTEGER,
            symbol_id INTEGER,
            FOREIGN KEY(board_id) REFERENCES board(id) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY(symbol_id) REFERENCES symbol(id) ON DELETE CASCADE ON UPDATE CASCADE,
            PRIMARY KEY(board_id, symbol_id)
        )''',
        '''CREATE TABLE IF NOT EXISTS symbol_connection (
            board_id INTEGER NOT NULL, 
            start_symbol INT NOT NULL, 
            destination_symbol INT NOT NULL, 
            PRIMARY KEY(start_symbol, destination_symbol),
            FOREIGN KEY(board_id) REFERENCES board(id) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY(start_symbol) REFERENCES symbol(id) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY(destination_symbol) REFERENCES symbol(id) ON DELETE CASCADE ON UPDATE CASCADE
        )''',
        "INSERT INTO board(name, description) VALUES('test_board', 'test_board');",
        "INSERT INTO symbol_type(type) VALUES('Event/basic');",
        "INSERT INTO symbol_type(type) VALUES('Event/conditioning');",
        "INSERT INTO symbol_type(type) VALUES('Event/intermediate');",
        "INSERT INTO symbol_type(type) VALUES('Event/remote basic');",
        "INSERT INTO symbol_type(type) VALUES('Event/underdeveloped');",
        "INSERT INTO symbol_type(type) VALUES('Gate/and');",
        "INSERT INTO symbol_type(type) VALUES('Gate/or');",
        "INSERT INTO symbol_type(type) VALUES('Gate/priority and');",
        "INSERT INTO symbol_type(type) VALUES('Gate/priority or');",
        "INSERT INTO symbol_type(type) VALUES('Gate/exclusive or');",
        "INSERT INTO symbol_type(type) VALUES('Transfer');",
        "INSERT INTO symbol(name, description, type) VALUES('Test event', 'test basic event', 1);",
        "INSERT INTO symbol(name, description, type) VALUES('Test and gate', 'test and gate', 6);",
        "INSERT INTO symbol(name, description, type) VALUES('Test intermediate event', 'test int event', 3);",
        "INSERT INTO symbol(name, description, type) VALUES('Test or gate', 'test or gate', 7);",
        "INSERT INTO board_symbol(board_id, symbol_id) VALUES(1, 1);",
        "INSERT INTO board_symbol(board_id, symbol_id) VALUES(1, 2);",
        "INSERT INTO board_symbol(board_id, symbol_id) VALUES(1, 3);",
        "INSERT INTO board_symbol(board_id, symbol_id) VALUES(1, 4);",
        "INSERT INTO symbol_connection(board_id, start_symbol, destination_symbol) VALUES(1, 1, 2);",
        "INSERT INTO symbol_connection(board_id, start_symbol, destination_symbol) VALUES(1, 1, 3);",
        "INSERT INTO symbol_connection(board_id, start_symbol, destination_symbol) VALUES(1, 3, 4);",
        "SELECT * FROM symbol_connection;",
        "SELECT * FROM symbol_type;",
        "SELECT * FROM board_symbol;",
        "SELECT * FROM symbol;",
        "SELECT * FROM board;"]

        for statement in statements:
            print(f"Executing {statement}")
            cursor.execute(statement)
            data = cursor.fetchall()
            print(data)
    except Exception as e: 
        print(e)
        # raise Exception("Problem initializing MySQL database - check that fault_tree database exists and user root has access")