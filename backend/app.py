from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


@app.route("/")
def home():

    return jsonify(
        message="Backend running in Kubernetes"
    )


@app.route("/api")
def api():

    return jsonify(
        status="success",
        message="Connected to backend"
    )


@app.route("/db")
def database():

    try:

        connection = mysql.connector.connect(
            host="mysql-service",
            user="root",
            password="mysqlpassword",
            database="mysql"
        )

        return jsonify(
            message="Database connection successful"
        )


    except Exception as e:

        return jsonify(
            error=str(e)
        )


app.run(
    host="0.0.0.0",
    port=5000
)
