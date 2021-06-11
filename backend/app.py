import json, os
import firebase_admin

from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_cors import CORS
from firebase_admin import auth
default_app = firebase_admin.initialize_app()


app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.urandom(24)

user = auth.create_user(
    email='user@example.com',
    email_verified=False,
    phone_number='+15555550100',
    password='secretPassword',
    display_name='John Doe',
    photo_url='http://www.example.com/12345678/photo.png',
    disabled=False)
    
print('Sucessfully created new user: {0}'.format(user.uid))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html",msg="")

    email = request.form['email']
    password = request.form['password']
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        session['usr'] = email
        return redirect(url_for('index'))
    except:
        return render_template("login.html", msg="メールアドレスまたはパスワードが間違っています。")

@app.route("/", methods=['GET'])
def index():
    usr = session.get('usr')
    if usr == None:
        return redirect(url_for('login'))
    return render_template("index.html", usr=usr)

@app.route('/logout')
def logout():
    del session['usr']
    return redirect(url_for('login'))

@app.route('/')
def hello_world():
    return "Hello Flask"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
