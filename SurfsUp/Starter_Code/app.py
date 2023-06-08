# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
import pandas as pd

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measr = Base.classes.measurement
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

@app .route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to the 'Home' page!<br/><br/>"
        f"Available routes: <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/<start> <br/>"
        f""
    )

# Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation():
    #create session
    session = Session(engine)

    #Query extracts last 12 months of data
    year = dt.date(2017,8,23) - dt.timedelta(days=365)
    sel = [Measr.date,
      Measr.prcp,]
    
    prev_year = session.query(*sel).\
    filter(Measr.date >= year).\
    order_by(Measr.date).all()

    #close session
    session.close()

    #convert results into dictionary
    all_precipitation = []
    for date, precipitation in prev_year:
        precipitation_dict = {}
        precipitation_dict['date'] = date
        precipitation_dict['preciptiation'] = precipitation
        all_precipitation.append(precipitation_dict)

    #return results on page in JSON
    return jsonify(all_precipitation)

# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    #create session
    session = Session(engine)

    stats = session.query(Station.station, Station.name).all()

    #close session
    session.close()

    all_station = list(np.ravel(stats))

    return jsonify(all_station)

# Query the dates and temperature observations of the most-active station for the previous year of data.
# Return a JSON list of temperature observations for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():
    #create session
    session = Session(engine)

    year = dt.date(2017,8,23) - dt.timedelta(days=365)

    most_active = session.query(Measr.date, Measr.tobs).\
    filter(Measr.date >= year). \
    filter(Measr.station == 'USC00519281').\
    order_by(Measr.date).all()

    #close session
    session.close()

    activity = list(np.ravel(most_active))

    return jsonify(activity)

# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
# For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
# For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
@app.route("/api/v1.0/<start>")
def start():
    #create session
    session = Session(engine)

    #close session
    session.close()
    return()

@app.route("/api/v1.0/<start>/<end>")
def end():
    #create session
    session = Session(engine)

    #close session
    session.close()
    return()


if __name__ == '__main__':
    app.run(debug=True)