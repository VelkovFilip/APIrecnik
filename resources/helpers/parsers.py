from flask_restful import reqparse
from flask_restful import inputs

device_parser = reqparse.RequestParser()
device_parser.add_argument("ip_address", type = str, help = "IP address of device required", required = True)
device_parser.add_argument("password", type = str, help = "Device password required", required = True)

device_link_parser = reqparse.RequestParser()
device_link_parser.add_argument("password", type = str, help = "Device password required", required = True)




user_put_args = reqparse.RequestParser()
user_put_args.add_argument("name", type = str, help = "Name of the User required!", required = True)
user_put_args.add_argument("surname", type = str, help = "Surname of the User required!", required = True)
user_put_args.add_argument("email", type = str, help = "Email of the user required!", required = True)
user_put_args.add_argument("password", type = str, help = "Password of the user required!", required = True)


login_put_args = reqparse.RequestParser()
login_put_args.add_argument("email", type = str, help = "Name of the User required!", required = True)
login_put_args.add_argument("password", type = str, help = "Password of the user required!", required = True)
login_put_args.add_argument("deviceID", type = str, help = "The device ID", required = False)




dict_parser = reqparse.RequestParser()
dict_parser.add_argument("mkd", type = str, required = True)
dict_parser.add_argument("mkd_exp", type = str, required = True)
dict_parser.add_argument("alb", type = str, required = True)
dict_parser.add_argument("alb_exp", type = str, required = True)
dict_parser.add_argument("validated", type = str, required = True)
dict_parser.add_argument("category", type = str, required = True)