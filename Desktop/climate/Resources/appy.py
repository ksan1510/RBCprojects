import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
       
        
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Lists all the precipitation data with the associated dates"""
    # Query
    results = session.query(Measurement.date, Measurement.prcp).all() 

    # Convert list of tuples into normal list
    all_prec = list(np.ravel(results))

    return jsonify(all_prec)


@app.route("/api/v1.0/stations")
def stations():
    """All stations"""
    # Query all stations
    station_results = session.query(Station.station).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    stations_list = list(np.ravel(station_results))

    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    """tobs"""
    # Query all stations
    station_tag = 'USC00519281'
    tobs_results = session.query(Measurement.tobs).filter(Measurement.station == station_tag).all()


    # Create a dictionary from the row data and append to a list of all_passengers
    tobs_list = list(np.ravel(tobs_results))

    return jsonify(tobs_list)




if __name__ == '__main__':
    app.run(debug=True)