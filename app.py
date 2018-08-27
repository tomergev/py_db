from flask import Flask, request
from routes.users import user_routes

app = Flask(__name__)

# Registering all the blueprints
app.register_blueprint(user_routes)

if __name__ == "__main__":
	app.run(debug=True)

