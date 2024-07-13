from flask import Flask, render_template, Blueprint, jsonify
import sqlite3

main = Blueprint('main', __name__)

@main.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

@main.route('/data')
def data():
    data = get_data()
    return jsonify(data)

def get_data():
    conn = sqlite3.connect('snmp_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM snmp_data")
    data = c.fetchall()
    conn.close()
    return data

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app

