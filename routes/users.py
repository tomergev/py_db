import sys
# Needing to add this append in order to get session from a different directory
sys.path.append("/home/tomer/py_db/")
from session import session # Importing the db session
from schemas.user import User # Importing the user schema
from flask import request, Blueprint # Flask imports

user_routes = Blueprint("user_routes", __name__, template_folder="templates")

# Stackover flow discussing flask routes: https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request
@user_routes.route("/users", methods=["POST"])
def post_user():
	print request.form
	return "Posting User"

@user_routes.route("/users", methods=["GET"])
def get_user():
	users = session.query(User).all()
	print users

	for user in users:
		print user["first_name"]

	return "Getting users"

# # Stackover flow discussing flask routes: https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request
# @app.route("/users", methods=["POST"])
# def parse_request():
# 	print request.form
# 	return "Hello World"



