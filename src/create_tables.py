import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host = os.getenv("DB_HOST"),
    port = os.getenv("DB_PORT"),
    database = os.getenv("DB"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASS")
)

cursor = conn.cursor()

with open("schema.sql", "r") as f:
    cursor.execute(f.read())

conn.commit()
cursor.close()
conn.close()
print("tables created successfully")