import pyrebase
from flask import *

app = Flask(__name__)

config = {
    "apiKey": "AIzaSyDjnoQLhs2r_-fUq-XjI4Jz3SnDPdebKUI",
    "authDomain": "test-f9a44.firebaseapp.com",
    "databaseURL": "https://test-f9a44.firebaseio.com",
    "projectId": "test-f9a44",
    "storageBucket": "test-f9a44.appsot.com",
    "messagingSenderId": "521401773960"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()



@app.route('/', methods=['GET','POST'])
def basic():
    unsuccessful = 'Please check yor credentials'
    successful = 'Login Successful'
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template('new.html', s=successful)
        except:
            return render_template('new.html', us=unsuccessful)

    return render_template('index.html')

if __name__ == "__main__":
    app.run()




# from flask import Flask, render_template, g, redirect, url_for
# from flask_oidc import OpenIDConnect
# from okta import UsersClient
#
# app = Flask(__name__)
# app.config["OIDC_CLIENT_SECRETS"] = "client_secrets.json"
# app.config["OIDC_COOKIE_SECURE"] = False
# app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
# app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
# app.config["SECRET_KEY"] = "LONG_RANDOM_STRING"
# oidc = OpenIDConnect(app)
# okta_client = UsersClient("dev-309226.oktapreview.com", "00m9PnDTVhU1gQA9ZiHz0pZZD2FhriO7hgzi3IBcV5")
#
# @app.before_request
# def before_request():
#     if oidc.user_loggedin:
#         g.user = okta_client.get_user(oidc.user_getfield("sub"))
#     else:
#         g.user = None
#
# @app.route('/')
# def index():
#     return render_template("index.html")
#
# @app.route("/dashboard")
# @oidc.require_login
# def dashboard():
#     return render_template("dashboard.html")
#
#
# @app.route("/login")
# @oidc.require_login
# def login():
#     return redirect(url_for(".dashboard"))
#
#
# @app.route("/logout")
# def logout():
#     oidc.logout()
#     return redirect(url_for(".index"))