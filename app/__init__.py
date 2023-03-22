from flask import Flask 




app = Flask(__name__)
app.config['SECRET_KEY'] = '88888888'


from app import routes 
