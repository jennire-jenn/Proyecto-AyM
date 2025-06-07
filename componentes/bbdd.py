import sqlite3

conn = sqlite3.connect('GravitySnake')

cursor = conn.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS jugadores(
    id INTEGER PRIMARY KEY,
    nombre varchar(15),
    score INTEGER DEFAULT 0  
    )

'''
)

def agregar(nombre):
    cursor.execute("INSERT INTO jugadores (nombre) VALUES (?)", (nombre))

def modificar(score,id):
    cursor.execute("UPDATE jugadores score=? WHERE id=?", (score,id))

def ver():
    cursor.execute("SELECT * FROM jugadores ORDER BY score DESC LIMIT 5")
    jugadores = cursor.fetchall()
    print(jugadores)
    return jugadores
