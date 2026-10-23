import sqlite3

conn = sqlite3.connect("chatbot.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS chats(
id INTEGER PRIMARY KEY,
User -> Hello
Bot -> Hi friend
)
""")

conn.commit()

conn.close()