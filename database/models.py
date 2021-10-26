from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
import datetime
from sqlalchemy_utils import EmailType
from flask import current_app as app


db = SQLAlchemy()


class DictRecnik(db.Model):
    __tablename__ = 'dict_recnik'
    id = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('dict_recnik_id_seq'::regclass)"))
    mkd = db.Column(db.String(30), nullable=False)
    mkd_exp = db.Column(db.String(150))
    alb = db.Column(db.String(30), nullable=False)
    alb_exp = db.Column(db.String(150))
    eng = db.Column(db.String(30), nullable=False)
    eng_exp = db.Column(db.String(150))
    validated = db.Column(db.Boolean())
    category = db.Column(db.String(30))










   



