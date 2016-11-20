from django.shortcuts import render
from django.http import HttpResponse
from .get_travel_time import get_traveltime
from .models import LargeTown, DistanceMatrix

def neighbours(center, time):

	def add_if(string, appendee):
		if len(appendee) > 0:
			string += ', ' + appendee
		return string

	# assume 100mph tops
	max_dist = 100* time / 60
	print(max_dist)

	# get destination from LargeTowns
	dest = LargeTown.objects.get(place_name = center)
	print(dest)

	t1 = DistanceMatrix.objects.filter(start=dest,
				linear_distance__lte=max_dist).values('end')
	t2 = DistanceMatrix.objects.filter(end=dest,
				linear_distance__lte=max_dist).values('start')
	# get all other towns within 100 miles

	query_points = []
	for v in t1:
		town = LargeTown.objects.get(place_name=v['end'])
		print("From %s to %s. %s miles" % (dest, town, DistanceMatrix.objects.get(start=dest,end=town)))
		s = town.place_name
		s = add_if(s, town.admin_name1)
		s = add_if(s, town.admin_name2)
		s = add_if(s, town.admin_name3)
		query_points.append( s )
	for v in t2:
		town = LargeTown.objects.get(place_name=v['start'])
		s = town.place_name
		s = add_if(s, town.admin_name1)
		s = add_if(s, town.admin_name2)
		s = add_if(s, town.admin_name3)
		query_points.append( s )

	return query_points


def results(request):
	dest = request.GET.get('destination')
	time = int(request.GET.get('time'))
	method = request.GET.get('optionsTransit')

	start_points = list(set(neighbours(dest, time)))


	names = start_points

	# dists = dict()
	# while len(start_points) > 25:
	# 	pts = start_points[0:25]
	# 	start_points = start_points[25:]
	# 	a = get_traveltime(pts, dest, method)
	# 	dists = dict(**dists, **a)

	# if len(start_points) > 0:
	# 	a = get_traveltime(start_points, dest, method)
	# 	dists = dict(**dists, **a)

	# filtered = {k:v for k, v in dists.items() if v < time*60}
	# names = list(filtered.keys())
	
	print("%d locations returned." % len(names))
	return render(request, 'traveltime/list_nearby.html', {'locations' : names})

def input(request):
	places = LargeTown.objects.all()
	start_points = []
	for place in places:
		s = place.place_name
		start_points.append(s)

	return render(request, 'traveltime/index.html', {'locations' : start_points})