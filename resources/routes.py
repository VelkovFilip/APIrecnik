from .dict import *



def initialize_routes(api):

	api.add_resource(WholeDict, "/all")
	api.add_resource(oneInput, "/single/<string:lang>/<string:word>")
	api.add_resource(InsertWord,'/insertWord')


