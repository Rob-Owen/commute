from django.shortcuts import render
from django.http import HttpResponse
from get_travel_time import get_traveltime
from .models import LargeTown, DistanceMatrix

def neighbours(center, time):

	# assume 100mph tops
	max_dist = time / 60 * 100

	# get destination from LargeTowns
	dest = LargeTown.objects.get(place_name = center)

	# get all other towns within 100 miles
	starts = DistanceMatrix.objects().filter(
		route_starts=dest, linear_distance__lte=max_dist)
	ends = DistanceMatrix.objects().filter(
		route_ends = dest, linear_distance__lte=max_dist)
	
	query_points = []
	for town in starts:
		query_points.append( town.place_name + ', ' +
							 town.admin_name1 + ', ' +
							 town.admin_name2 + ', ' +
							 town.admin_name3 )
	for town in ends:
		query_points.append( town.place_name + ', ' +
							 town.admin_name1 + ', ' +
							 town.admin_name2 + ', ' +
							 town.admin_name3 )

	return query_points


def results(request):
	dest = request.GET.get('destination')
	time = int(request.GET.get('time'))
	method = request.GET.get('optionsTransit')

	start_points = neighbours(dest, time)

	return render(request, 'traveltime/nearby_towns.html', {'locations' : start_points})

#	while len(start_points) > 25:
#		pts = start_points[0:25]
#		start_points = start_points[25:]
#		get_traveltime(start_points, dest, method):
#	if len(start_points) > 0:
#		get_traveltime(start_points, dest, method):


def input(request):
	places = LargeTown.objects.all()
	start_points = []
	for place in places:
		s = place.place_name
		if place.admin_name1 is not None:
			s += ', ' + place.admin_name1
		if place.admin_name2 is not None:
			s += ', ' + place.admin_name2
		if place.admin_name3 is not None:
			s += ', ' + place.admin_name3
		start_points.append(s)

	s = []
	for i, s in enumerate(start_points):
		s.append({ 'text' 	: s,
					'value' : i	})

	return render(request, 'traveltime/index.html', {'locations' : s})