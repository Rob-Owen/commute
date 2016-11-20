def dist_calc():
	"""
	Calculate distance between all location pairs 
	"""

	from geopy.distance import vincenty
	import sys
	import os
	your_djangoproject_home="./commute"
	sys.path.append(your_djangoproject_home)
	os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

	import django
	django.setup()

	from traveltime.models import LargeTown, DistanceMatrix

	done = []
	for p1 in LargeTown.objects.all():
		print(p1.place_name)
		for p2 in LargeTown.objects.all():
			origin = (float(p1.latitude), float(p1.longitude))
			dest = (float(p2.latitude), float(p2.longitude))
			dist = vincenty(origin, dest).miles
			n = DistanceMatrix( 
				start=p1,
				end=p2,
				linear_distance=dist )
			n.save()
			done.append({p1.place_name, p2.place_name})

if __name__ == '__main__':
    dist_calc()