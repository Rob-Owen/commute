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
		n = DistanceMatrix( linear_distance=dist )
		n.save()
		p1.route_starts = n
		p2.route_ends = n
		p1.save()
		p2.save()
		done.append({p1.place_name, p2.place_name})