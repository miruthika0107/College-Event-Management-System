from flask import Flask
import sqlite3

app = Flask(__name__)


def init_db():
    connection = sqlite3.connect("college_events.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            student_id TEXT UNIQUE NOT NULL,
            department TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


@app.route("/")
def home():
    return "College Event Management System Backend is Running!"


if __name__ == "__main__":
    init_db()
    app.run(debug=True)