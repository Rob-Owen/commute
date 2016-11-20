from geopy.distance import vincenty
import sys
import os
your_djangoproject_home="./commute"
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()

from traveltime.models import Population, uk_location, LargeTown

for town in Population.objects.all():
	loc = town.location
	if town.pop < 10000 or loc is None:
		continue

	nt = LargeTown(
			place_name = loc.place_name,
			admin_name1 = loc.admin_name1,
			admin_name2 = loc.admin_name2,
			admin_name3 = loc.admin_name3,
			latitude = loc.latitude,
			longitude = loc.longitude,
			pop = town.pop
		)
	nt.save()