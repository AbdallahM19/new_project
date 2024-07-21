from flask import Flask, jsonify, render_template, request
from sys import modules
from blueprints_data import *


app = Flask(__name__)
app.register_blueprint(users_dp)


@app.route('/', methods=['GET'])
@app.route('/', methods=['POST'])
@app.route('/', methods=['DELETE'])
def home_page():
    """Home"""
    if request.method == 'GET':
        return jsonify({'message': 'Home Page - GET'})
    elif request.method == 'POST':
        return jsonify({'message': 'Home Page - POST'})
    elif request.method == 'DELETE':
        return jsonify({'message': 'Home Page - DELETE'})
    else:
        return jsonify({'error': 'Method not allowed'}), 405


@app.route('/login/', methods=['GET', 'POST'])
def login():
    """login page"""
    return jsonify({'message': 'Login - POST'})


@app.route('/register/', methods=['GET', 'POST'])
def register():
    """register"""
    return jsonify({'message': 'Register - POST'})


if __name__ == "__main__":
    print(dir())
    # for i in dir():
    # for i in locals():
    # for i in globals():
    # for i in vars(object):
        # print(i)
    # app.run(host="127.0.0.1", port=5000, debug=True)