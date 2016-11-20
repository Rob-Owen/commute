import googlemaps
from datetime import datetime
from .api_key import key

# Test: Variables to be received from database
origin = ["Fakenham", "Staplehurst"]
dest = "Oxford"
method = "transit"

def get_traveltime(origin, dest, method):
	""" 
	Use Maps Distance Matrix API to calculate travel time

	origin = list of strings (max 25)
	dest = string
	method = string, "transit", "driving", "bicycling", "walking"

	Returns dictionary with keys corresponding to input origin list entries and 
	values of travel time in seconds.
	"""

	# Create gmaps client
	gmaps = googlemaps.Client(key=key)

	# Force time to Monday 8am TODO: Lazy and time specific
	dt = datetime(2016, 11, 21, 8, 0, 0)
	seconds = dt.timestamp()

	# Request travel time
	distance_result = gmaps.distance_matrix(origin, dest, mode=method, units="imperial", departure_time=seconds)
	# Store in dictionary
	distance_dict = dict()

	for i, start in enumerate(origin):
		# Extract time in seconds and store in dict with relevant origin name
		try:
			distance_dict[start] = distance_result["rows"][i]["elements"][0]["duration"]["value"]
		except:
			print("Failed to find distance from %s to %s" % (start, dest))

	return distance_dict
