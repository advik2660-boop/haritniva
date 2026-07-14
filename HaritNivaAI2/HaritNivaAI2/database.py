import sqlite3

DATABASE_NAME = "database.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS farmer(
            
               id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    username TEXT NOT NULL,
    contact TEXT NOT NULL,
    farm_name TEXT NOT NULL,
    state TEXT NOT NULL,

    nitrogen REAL DEFAULT 300,
    phosphorus REAL DEFAULT 60,
    potassium REAL DEFAULT 280,
    sulfur REAL DEFAULT 20,
    organic_carbon REAL DEFAULT 1.0,
    zinc REAL DEFAULT 1.2,
    iron REAL DEFAULT 4.5,
    ph REAL DEFAULT 6.8 
            
        )
    """)

    connection.commit()
    connection.close()


def save_farmer(name, username, contact, farm_name, state):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM farmer")

    cursor.execute("""
        
        INSERT INTO farmer(
            name,
            username,
            contact, 
            farm_name,
            state,
            nitrogen,
            phosphorus,
            potassium,
            sulfur,
            organic_carbon,
            zinc,
            iron,
            ph
        )
        VALUES(
        ?, ?, ?, ?, ?,
              300,
              60,
              280,
              20,
              1.0,
              1.2,
              4.5,
              6.8
        )
    """,(name, username, contact, farm_name, state))

    connection.commit()
    connection.close()


def get_farmer():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
name,
username,
contact,
farm_name,
state,
nitrogen,
phosphorus,
potassium,
sulfur,
organic_carbon,
zinc,
iron,
ph
FROM farmer    
                   """)

    farmer = cursor.fetchone()

    connection.close()

    return farmer