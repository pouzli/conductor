import sqlite3

def init_db():
    conn = sqlite3.connect('conductor.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        telegram_id INTEGER UNIQUE,
        name TEXT,
        age INTEGER
    )
    ''')
    conn.commit()
    conn.close()

def add_user(telegram_id, name, age):
    conn = sqlite3.connect('conductor.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO users (telegram_id, name, age) VALUES (?, ?, ?)',
                   (telegram_id, name, age))
    conn.commit()
    conn.close()

def get_user(telegram_id):
    conn = sqlite3.connect('conductor.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE telegram_id = ?', (telegram_id,))
    user = cursor.fetchone()
    conn.close()
    return user
