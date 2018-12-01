from flask import Flask, jsonify, request
import mysql.connector
import json

app = Flask(__name__)


@app.route('/tennis/player')
def find_players():
    pass


@app.route('/tennis/category')
def find_categories():
    pass


@app.route('/tennis/schedule')
def find_matches_schedule():
    pass


if __name__ == "__main__":
    app.run(debug=True)
