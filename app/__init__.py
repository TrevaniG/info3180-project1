from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "cheiu9794749hfriehnr4349"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
app.config['ALLOWED_UPLOADS'] = set(['png','jpg','jpeg'])




db = SQLAlchemy(app)
app.config.from_object(__name__)
from app import views
