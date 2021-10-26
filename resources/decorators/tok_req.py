# from database.models import User
# from functools import wraps
# from flask import request
# from flask_restful import abort


# def token_required(f):
#   @wraps(f)
#   def decorator(*args,**kwargs):
#     token = None
#     if 'token' in request.headers:
#       token = request.headers['token']

#     if not token:
#       return abort(409, message = 'No token provided!')

#     user_id = User.decode_auth_token(token)
#     if isinstance(user_id, str):
#       return abort(409, message = user_id)

#       return f(*args,**kwargs)
#     return f(*args, **kwargs, user_id = user_id)
#   return decorator

