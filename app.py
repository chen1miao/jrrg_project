import os
from flask import Flask, request, session, jsonify, send_file
from flask_cors import CORS
from db import app, execute_sql_query  #  ensure you have implemented execute_sql_query correctly

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)  # enable CORS for all routes

def getresponse(code=200, msg=None, data=None):
    res = {
        "code": code,
        "msg": msg,
        "data": data
    }
    return jsonify(res)

@app.route('/register', methods=['POST'])
def register():
    print(request.json)
    username = request.json['username']
    password = request.json['password']
    existing_user_sql = "SELECT * FROM user WHERE username = %s"
    existing_user_params = (username,)
    existing_user = execute_sql_query(existing_user_sql, existing_user_params, fetchone=True)

    if existing_user:
        return getresponse(400, "Username already exists")

    insert_user_sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
    insert_user_params = (username, password)
    execute_sql_query(insert_user_sql, insert_user_params)

    return getresponse(200, "Registration successful")

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    existing_user_sql = "SELECT * FROM user WHERE username = %s"
    existing_user_params = (username,)
    existing_user = execute_sql_query(existing_user_sql, existing_user_params, fetchone=True)

    sql = "SELECT * FROM user WHERE username = %s"
    params = (username, )
    user = execute_sql_query(sql, params, fetchone=True)

    if user :
        if user['password'] == password:
            print(user['username'], user['id'])
            session['user'] = user
            return getresponse(200, "Login successful", {"user": username, "id": user['id'],"pw":password})
        else:
            return getresponse(400, "密码错误")
        
    else:
        return getresponse(400, "用户名不存在")

@app.route('/change', methods=['POST'])
def change():
    print(request.json)
    username = request.json['username']
    password = request.json['password']
    existing_user_sql = "SELECT * FROM user WHERE username = %s"
    existing_user_params = (username,)
    existing_user = execute_sql_query(existing_user_sql, existing_user_params, fetchone=True)


    '''insert_user_sql = "UPDATE user SET password={password} WHERE username= %s"
    execute_sql_query(insert_user_sql)'''
    insert_user_sql = "UPDATE user SET password=%s WHERE username=%s"
    params = (password, username)
    execute_sql_query(insert_user_sql, params)

    return getresponse(200, "Registration successful")

@app.route('/logout')
def logout():
    session.clear()
    return getresponse(200, "Logout successful")

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    uploads_dir = 'uploads'
    file_path = os.path.join(uploads_dir, filename)
    return send_file(file_path, as_attachment=True)

@app.route('/uploads', methods=['POST'])
def uploads_file():
    file = request.files['file']
    file_path = save_file(file)
    return jsonify({'file_path': file_path}), 201

def save_file(file):
    if not os.path.exists('uploads'):
        os.mkdir('uploads')
    file_path = f'uploads/{file.filename}'
    file.save(file_path)
    file_path = file_path.replace("uploads/", "http://127.0.0.1:5001/download/")
    return file_path

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
