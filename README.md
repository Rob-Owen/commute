# Commute

A web app for calculating potential places to live based on your work location, method of transport and maximum travel time. Alongside these results, visualises demographic data from the Esri OpenData service. Location lat/lon sourced from [GeoNames](http://www.geonames.org/).

Built at [OxfordHack 2016](https://devpost.com/software/commute).

## Installation and Usage

Using Python 3, install `requirements.txt` using pip:

```
pip install -r requirements.txt
```

In the directory `traveltime` add a file api_key.py which contains a variable `key="your-google-maps-api-key"`, which must be enabled for use with the Google Maps Distance Matrix API.

To run:

```
python manage.py runserver
```

If you want/need to rebuild the databse:

1. Run the python script `build_database.py` in the `db-build` directory.

2. Run the following commands:

```
python manage.py makemigrations
python manage.py migrate 
```

3. You can now add a superuser to view the database at /admin:

```
python manage.py createsuperuser
```


## Inspiration

People don't always live where they work, but also don't want to spend too long on the train or in the car to get there. This is a problem we are now facing after graduation and finding jobs in new places. If you know two locations it is easy enough to query directly, but with hundreds of places within a reasonable distance, it is very difficult to work out the best options. Commute allows you to input your workplace, an amount of time you are willing to commute for and a method of transport. 

## What it does

Given your work destination, choose how you would like to commute and the maximum amount of time you are willing to travel. Commute will show a map of potential places to live, with options to visualise layers of geographic data from ArcGIS OpenData in .geojson format.

## How we built it

We aggregated data from a number of sources on UK locations in order to build a database of locations, names, population sizes and distances. This allowed us to filter the number of queries beign passed to the Google Maps Distance Matrix to improve loading times (and save requests to our API key!) After getting the travel time with Google, we then plotted the map on the front end with the Esri API and used their layers and OpenData to add contextual information.

## Challenges we faced

Finding reliable data on place names in usable formats was difficult. We used a .csv file from GeoNames and an excel spreadsheet from a Government FOI request. Parsing this data and storing it in the database in an efficient way was one of the biggest challenges.

## Accomplishments we're proud of

Producing a list of reasonable results in a reasonable time, for a genuine problem we have recently experienced. It was fun to see locations along the main train lines highlighted - also highlights the limitations of public transport in rural areas!

## What we learned

Neither of us had much prior experience in javascript, so using the Esri API was a challenge but a rewarding one.

## What's next

We want to add a number of features - house price data particularly would make the tool much more useful to a wider audience. We would also like to find more data sources and allow the user to filter the results based on these. Finally, we'd like to add a second destination option, for couples who want to find somewhere central to live.