from flask import Flask
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = mysql.connector.connect(
            host = "db",
            user = "root",
            password = os.environ.get('password'),
            database = os.environ.get('dbname')
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hello This is working due to Docker Compose. Thank You Docker Compose'")
        msg = cursor.fetchone()[0]
        conn.close()
        return msg
    except Exception as e:
        return f"Error:{e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)