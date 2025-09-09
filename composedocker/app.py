from flask import Flask,render_template
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = mysql.connector.connect(
            host = "db",
            user = "root",
            password = os.environ.get("password"),
            database = os.environ.get("dbname")
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM chocolates")
        msg = cursor.fetchall()
    except Exception as e:
        return f"Error as {e}"
    return render_template("index.html",msg = msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)