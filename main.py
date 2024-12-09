from fastapi import FastAPI
from db import get_db_connection

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Welcome to FastAPI with Postgresql"}

@app.get("/users")
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    conn.close()
    return {"users":users}
