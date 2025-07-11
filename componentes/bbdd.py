import sqlite3

conn = sqlite3.connect('GravitySnake.db')
cursor = conn.cursor()
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS jugadores(
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(100),
    score INTEGER DEFAULT 0  
    )
'''
)

def agregar(nombre):
    #cursor.execute("INSERT INTO jugadores (nombre) VALUES (?)", (nombre))
    cursor.execute("INSERT INTO jugadores (nombre) VALUES (?)", (nombre,))
    conn.commit()


def modificar(score,id):
    #cursor.execute("UPDATE jugadores score=? WHERE id=?", (score,id))
    cursor.execute("UPDATE jugadores SET score=? WHERE id=?", (score, id))
    conn.commit()

def ver():
    cursor.execute("SELECT * FROM jugadores ORDER BY score DESC LIMIT 5")
    jugadores = cursor.fetchall()
    print(jugadores)
    return jugadores

def veractual():
    cursor.execute("SELECT * FROM jugadores ORDER BY id DESC LIMIT 1")
    jugadores = cursor.fetchall()
    print(jugadores)
    return jugadores
