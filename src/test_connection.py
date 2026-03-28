import os 
#from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import psycopg2

load_dotenv()
#calling from env file
def get_connection():
    conn = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        database = os.getenv("DB"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASS")
    )
    return conn

try:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    print("Connection successful")
    cursor.close()
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")
