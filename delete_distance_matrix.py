from geopy.distance import vincenty
import sys
import os
your_djangoproject_home="./commute"
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()

from traveltime.models import DistanceMatrix

DistanceMatrix.objects.all().delete()
