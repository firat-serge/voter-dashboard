from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# import os

DB_CONFIG = {
    "database": "data",
    "username": "postgres",
    "password": "19820815",
    "host": "localhost",
    "port": "5432"}

# Notice, normally this is set with environment variables on the server
# machine do avoid exposing the credentials. Something like
# DB_CONFIG = {}
# DB_CONFIG['database'] = os.environ.get('DATABASE')
# DB_CONFIG['username'] = os.environ.get('USERNAME')
# ...

# Create a flask application
app = Flask(__name__)

# Set the database connection URI in the app configuration

username = DB_CONFIG['username']
password = DB_CONFIG['password']
host = DB_CONFIG['host']
port = DB_CONFIG['port']
database = DB_CONFIG['database']

database_uri = f"postgresql://{username}:{password}@{host}:{port}/{database}"

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

# Create object to control SQLAlchemy from the Flask app
db = SQLAlchemy(app)

# Create a data model object that matches our database
# Matches rides_geojson view 

class votes_geojson(db.Model):
    __tablename__ = "votes_geojson_test1"
    __table_args__ = {"schema": "sa"}
    
    Plaka = db.Column(db.Integer, primary_key=True)
    Y_18 = db.Column(db.Float)
    NUTS3_1 = db.Column(db.Text)
    ADMIN_NAME = db.Column(db.Text)
    PopDen = db.Column(db.Float)
    Hedu = db.Column(db.Float)
    AKP_per = db.Column(db.Float)
    MHP_per = db.Column(db.Float)
    HUDA_PAR_per = db.Column(db.Float)
    VP_per = db.Column(db.Float)
    HDP_per = db.Column(db.Float)
    CHP_per = db.Column(db.Float)
    SP_per = db.Column(db.Float)
    IYIP_per = db.Column(db.Float)
    INDP_per = db.Column(db.Float)
    geojson = db.Column(db.Text)

    

    # Because we want to use this object to insert data into the database
    # We need to be able to create an object from the POST request body
    def __init__(self, Y_18, ADMIN_NAME, NUTS3_1, PopDen, Hedu, AKP_per, MHP_per, HUDA_PAR_per, VP_per, HDP_per, CHP_per, SP_per, IYIP_per, INDP_per ):
        self.Y_18 = Y_18
        self.NUTS3_1 = NUTS3_1
        self.ADMIN_NAME = db.Column(db.Text)
        self.PopDen = PopDen
        self.Hedu = Hedu
        self.AKP_per = AKP_per
        self.MHP_per = MHP_per
        self.HUDA_PAR_per = HUDA_PAR_per
        self.VP_per = VP_per
        self.HDP_per = HDP_per
        self.CHP_per = CHP_per
        self.SP_per = SP_per
        self.IYIP_per = IYIP_per
        self.INDP_per = INDP_per

# TEST
@app.route('/')
def home():
  return("Hello world")

# @app.route('/votes_geojson/<ADMIN_NAME>', methods=['GET'])
# def get_ride2(ADMIN_NAME):
#     ride = votes_geojson.query.get(ADMIN_NAME)
#     del ride.__dict__['_sa_instance_state']
#     return jsonify(ride.__dict__)

# GET method to get a single province using it's id from the votes_geojson view
@app.route('/votes_geojson/<Plaka>', methods=['GET'])
def get_vote(Plaka):
    ride = votes_geojson.query.get(Plaka)
    del ride.__dict__['_sa_instance_state']
    return jsonify(ride.__dict__)

# GET method to get all votes from the votes_geojson view
@app.route('/votes_geojson', methods=['GET'])
def get_votes():
  rides = []
  for ride in db.session.query(votes_geojson).all():
    del ride.__dict__['_sa_instance_state']
    rides.append(ride.__dict__)
  return jsonify(rides)




if __name__ == '__main__':
    
    app.run(debug=True)