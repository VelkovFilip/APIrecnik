
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with, marshal
from flask_sqlalchemy import SQLAlchemy
from collections import OrderedDict
from sqlalchemy import orm
from flask_migrate import Migrate
from flask_cors import CORS
from database.models import db
from resources.routes import initialize_routes


app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password123@104.248.34.197:5430/Recnik'
app.config['SQLALCHEMY_ECHO'] = True




migrate = Migrate(app, db)
db.init_app(app)
initialize_routes(api)




if __name__ == "__main__":
    app.run(debug=True)