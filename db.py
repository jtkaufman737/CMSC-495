from flask import Flask 
from flaskext.mysql import MySQL 

mysql = MySQL() 

def create_db(app):
    app.config["MYSQL_DATABASE_USER"] = "root" 
    app.config["MYSQL_DATABASE_PASSWORD"] = "mysqluser" 
    app.config["MYSQL_DATABASE_DB"] = "fault_tree" 
    app.config["MYSQL_DATABASE_HOST"] = "localhost"  

    mysql.init(app)
    return mysql 

def seed_db(cursor):
    cursor.execute("""
    
    
    
    """)