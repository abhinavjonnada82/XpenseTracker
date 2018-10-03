import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("./serviceAccountCredentials.json")
firebase_admin.initialize_app(cred, {
   "databaseURL": "https://pythontest-3f926.firebaseio.com"
})

ref = db.reference('server/blog')
print(ref.get())
users_ref = ref.child('users')
users_ref.set({
    'alan' :{
        'date':"june",
        'time':'partytime'
    }
})



# import pyrebase
# import os
#
# config = {
#     "apiKey": "AIzaSyCVII4Y1lOdV7glRSw7fI9jspWav9-KbYs",
#     "authDomain": "pythontest-3f926.firebaseapp.com",
#     "databaseURL": "https://pythontest-3f926.firebaseio.com",
#     "projectId": "pythontest-3f926",
#     "storageBucket": "pythontest-3f926.appspot.com",
#     "messagingSenderId": "242054032933",
#     "serviceAccount": os.getcwd()+"/serviceAccountKey.json"
#   };
#
# firebase = pyrebase.initialize_app(config)
# db = firebase.database()
# auth = firebase.auth()
# #authenticate a user
# user = auth.sign_in_with_email_and_password("test@test.com", "test123")
#
#
# data = {"name":"Lane Kane"}
# results= db.child("users").child("Morty").set(data, user['idToken'])
#
# print (results)