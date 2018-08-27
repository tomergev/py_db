# Importing necessary variables
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 

# Importing the Base
from base import Base

# Creating the DB and starting a session
engine = create_engine("sqlite:///:syscoin_db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()

# user = User({
# 	"id": 11,
# 	"first_name": "Tomer",
# 	"last_name": "Gev"
# })
# session.add(user)
# session.commit()

# users = session.query(User).all()

# for user in users:
# 	print user

# session.close()