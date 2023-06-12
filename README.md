# 10-Module-sqlalchemy-challenge
Week 10 - SQLAlchemy

In this challenge we use SQLAlchemy to and Flask to execute a climate analysis on Hawaii data from a SQLite database.

To start the dependencies are imported from matplotlib, numpy, pandas, datetime and sqlalchemy.<br><br>


## Analyze and Explore the Climate Data

Using SQLAlchemy an engine is created to the SQLite database, reflected to a new model, and classes are extracted.<br><br>

Using the extracted classes, a reference to each table is saved and a session is created from Python to the Database.<br><br>

The table columns are inspected using the inspector tool and a query is executed to identify the most recent date in the data set and the day one year from the most recent date is calculated.

Another query is executed to retrieve the data and precipitation scores for one year's worth of data. (Date range from the day one year from the most recent date to the most recent date included in the data set)<br><br>

The query results are saved into a Pandas dataframe with the date data converted into date type, the columns are renamed and the data is sorted by the date.<br><br>

Pandas Plotting with Matplotlib is used to plot the data to show inches of precipitation within the date range and the summary statistics are calculated.<br><br>



## Exploratory Station Analysis

The station table columns and content are inspected/reviewed and a query is run to calculate the total number of stations int eh dataset.<br><br>

Another query is run to calculate the most active stations in the data set counting the total rows of data for each station and sorted from most to least active.<br><br>

Using the most active station (USC00519281), the lowest, highest and average temperatures are calculated.
Additionally, previous 12 months of data is queried for the most active station Additionally and the data is converted into a Pandas DataFrame and the results are plotted as a histogram.<br><br>

Finally, the session is closed.<br><br>

## Design the Climate App

To create the Climate App, the dependencies are loaded from numpy, sqlalchemy, datetime, pandas and flask.<br><br>

### Setting up the database
The engine is created, the existing database is reflected into a new model and the tables are reflected.<br>

A reference to each table is saved, the session is created and Flask is set up.<br><br>

### Home Page
The home page is set up/defined and returns a list of all the available routes.<br>


### /api/v1.0/precipitation
The precipitation page is set up/defined using the query results from the precipitation analysis and converted into a dictionary using date as the key and the prcp as the value. <br><br>

A session is created, query is executed to extract the data between one year from the most recent date to the most recent date and the session is closed.<br><br>

The results are converted into a dictionary and jsonified results are returned on the page.<br><br>

### /api/v1.0/stations
The stations page is set up/defined to return a JSON list of stations from the data set.<br><br>

A session is created, a query is executed to retrieve the station data, and the session is closed.<br><br>

The jsonified results are returned on the page.<br><br>

### /api/v1.0/tobs
The tobs page is set up/defined to return the dates and temperature observations of the most-active station for the previous year of data.<br><br>

a session is created, the 12 months of data is calculated and queried for the most active station and the session is closed.<br><br>

The jsonified results are returned on the page.<br><br>


### /api/v1.0/start
the start page is set up/defined to calculate the Minimum, Maximum and Average temperature for the specified start date.<br><br>

The session is created, the start date parameters are defined and a query is executed to calculate the Minimum, Maximum and Average temperatures for the start date. The session is closed.<br><br>

The jsonified results are returned on the page.<br><br>

  
### /api/v1.0/start/end
The start/end page is set up/defined to calculate the Minimum, Maximum and Average temperatures for the specified start-end range.<br><br>

A session is created, the start and end date parameters are defined and a query is executed to calculate the Minimum, Maximum and Average temperatures for the start-end range. The session is closed.<br><br>

The jsonified results are returned on the page<br><br>




