import driver
from database import Database as db
from project import Project
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        cursor = db.user_collection.find({'username': request.form['username']})  # find the user doc with the token
        for temp in cursor:
            actual_password = temp['password']
        if request.form['password'] == actual_password:
            return "pass"
        return "fail"
    else:
        return render_template('login.html')
