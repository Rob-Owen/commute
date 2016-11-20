from django.shortcuts import render
from django.http import HttpResponse
from .get_travel_time import get_traveltime
from .models import LargeTown, DistanceMatrix, CachedDistanceQuery
import pprint

def neighbours(center, time):

	def add_if(string, appendee):
		if len(appendee) > 0:
			string += ', ' + appendee
		return string

	# assume 100mph tops
	max_dist = 100* time / 60
	# get destination from LargeTowns
	dest = LargeTown.objects.get(place_name = center)
	t1 = DistanceMatrix.objects.filter(start=dest,
				linear_distance__lte=max_dist).values('end')
	t2 = DistanceMatrix.objects.filter(end=dest,
				linear_distance__lte=max_dist).values('start')
	# get all other towns within 100 miles

	query_points = []
	for v in t1:
		town = LargeTown.objects.get(place_name=v['end'])
		s = town.place_name
		s = add_if(s, town.admin_name3)
		s = add_if(s, town.admin_name2)
		s = add_if(s, town.admin_name1)
		query_points.append( s )
	for v in t2:
		town = LargeTown.objects.get(place_name=v['start'])
		s = town.place_name
		s = add_if(s, town.admin_name3)
		s = add_if(s, town.admin_name2)
		s = add_if(s, town.admin_name1)
		query_points.append( s )

	return set(query_points), dest.longitude, dest.latitude


def results(request):
	dest = request.GET.get('destination')
	time = int(request.GET.get('time'))
	method = request.GET.get('optionsTransit')

	n_details = neighbours(dest, time)

	start_points = list(n_details[0])
	query_points = []
	names = []
	times = []
	c = 0
	q = 0

	# check for cached results first
	cached = CachedDistanceQuery.objects.all()
	for place in start_points:
		tmp = cached.filter(start=place,end=dest)
		if len(tmp) == 1:
			names.append(place) 
			times.append(tmp[0].time)
			c += 1
		else:
			query_points.append(place)
			q += 1

	# google query for remaining places
	while len(query_points) > 25:
		pts = query_points[0:25]
		query_points = query_points[25:]
		a = get_traveltime(pts, dest, method)
		for k, v in a.items():
			names.append(k)
			times.append(v)
			s = CachedDistanceQuery(
					start=k,
					end=dest,
					time=v)
			s.save()

	if len(query_points) > 0:
		a = get_traveltime(query_points, dest, method)
		for k, v in a.items():
			names.append(k)
			times.append(v)
			s = CachedDistanceQuery(
					start=k,
					end=dest,
					time=v)
			s.save()

	for i, s in enumerate(names):
		print("%s: %d seconds" % (s, times[i]))

	names = [n for i,n in enumerate(names) if times[i] < 60*time]
	times = [t for t in times if t < 60*time]

	print("%d locations returned." % len(names))
	print("%d queries, %d cached" % (q, c))
	return render(request, 'traveltime/list_nearby.html', {'locations' : names,
														   'travel_times' : times,
														   'end_lat' : n_details[2],
														   'end_long' : n_details[1]})

def input(request):
	places = LargeTown.objects.all()
	start_points = []
	for place in places:
		s = place.place_name
		start_points.append(s)

	return render(request, 'traveltime/index.html', {'locations' : start_points})