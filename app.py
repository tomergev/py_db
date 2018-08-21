from flask import Flask, request

app = Flask(__name__)

# Stackover flow discussing flask routes: https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request
@app.route("/users", methods=["POST"])
def parse_request():
	print request.form
	print request.get_json(force=True)
	return "Hello World"

if __name__ == "__main__":
	app.run(debug=True)

# # Importing necessary variables
# from sqlalchemy import create_engine 
# from sqlalchemy.orm import sessionmaker 

# # Importing the Base
# from base import Base
# # Importing Schemas
# from schemas.user import User

# # Creating the DB and starting a session
# engine = create_engine("sqlite:///:syscoin_db", echo=True)
# Base.metadata.create_all(bind=engine)
# Session = sessionmaker(bind=engine)

# session = Session()

# user = User({
# 	"id": 11,
# 	"first_name": "Tomer",
# 	"last_name": "Gev"
# })
# session.add(user)
# session.commit()

# session.close()