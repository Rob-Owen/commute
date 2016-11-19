

# Full path and name to your csv file
csv_filepathname="pop.csv"
# Full path to your django project directory
your_djangoproject_home="./commute"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()

from traveltime.models import Population

import csv
dataReader = csv.reader(open(csv_filepathname))

for row in dataReader:
	table = Population()

	s = row[0]
	table.pop = row[1]

	words = s.split(' ')
	place = ' '.join(words[:-1]).strip()
	code = words[-1].strip()

	if code == 'BUA':
		table.place_name = place

	elif code == 'BUASD':
		a = place.split(' - ')
		authority = a[0].strip()
		location = a[1].strip()

		table.place_name = location
		table.region_name = authority
	else:
		print("Unrecognised code: %s" % code)

	try:
		table.save()
	except ValueError:
		print("Fail! " + row[0])
