from database.models import db,DictRecnik
from flask_restful import Resource, reqparse, abort, fields, marshal_with, marshal
from flask import make_response, jsonify
from resources.helpers.resource_files import *
from resources.helpers.parsers import dict_parser


class WholeDict(Resource):
	
	@marshal_with(dict_fields)
	def get(self):
		objs = DictRecnik.query.all()
		return objs


class oneInput(Resource):

	@marshal_with(dict_fields)
	def get(self, lang, word):
		word = word.capitalize()
		#return {'obj': word}
		if lang == 'mkd':
			obj = DictRecnik.query.filter_by(mkd = word).first()
		elif lang == 'eng':
			obj = DictRecnik.query.filter_by(eng = word).first()
		else:
			obj = DictRecnik.query.filter_by(alb = word).first()

		return obj


	 


class InsertWord(Resource):

	@marshal_with(dict_fields)
	def put(self):
		args = dict_parser.parse_args()
		tip1 = DictRecnik.query.filter_by(mkd = args['mkd'], category = args['category']).first()
		tip2 = DictRecnik.query.filter_by(alb = args['alb'], category = args['category']).first()
		if tip1 or tip2:
			return abort(409, message = "Word already exists!")
		val = False
		if args['validated'] == 'True':
			val = True
		zbor = DictRecnik(mkd = args['mkd'], mkd_exp = args['mkd_exp'],alb = args['alb'], alb_exp = args['alb_exp'], validated = val, category = args['category'])
		db.session.add(zbor)
		db.session.commit()
		return zbor




 