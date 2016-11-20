import sys
import os
your_djangoproject_home="./commute"
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()

from traveltime.models import LargeTown

LargeTown.objects.all().delete()
