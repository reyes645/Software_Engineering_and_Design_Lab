import driver
from database import Database as db
from project import Project
from flask import Flask, request, jsonify, render_template
# from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)

someuserdocument = {

}

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # cursor = db.user_collection.find({'username': request.form['username']})  # find the user doc with the token
        # for temp in cursor:
            # actual_password = temp['password']
        # if request.form['password'] == actual_password:
            #return "pass"

        uname = request.json.get('username')
        pword = request.json.get('password')

        return {
            "status": "fail",
            "user_document": someuserdocument,
            "given username": uname,
            "given password": pword
        }
    else:
        return render_template('login.html')

app.run(debug = True, host='0.0.0.0', port=8080)
