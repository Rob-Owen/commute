

# Full path and name to your csv file
csv_filepathname="/Users/rebeccamorgan/Drive/Development/commute/GB.txt"
# Full path to your django project directory
your_djangoproject_home="/Users/rebeccamorgan/Drive/Development/commute/commute"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()

from traveltime.models import uk_location

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter='\t', quotechar='"')

for row in dataReader:
	table = uk_location()

	table.country_code = row[0]
	table.postal_code = row[1]
	table.place_name = row[2]
	table.admin_name1 = row[3]
	table.admin_code1 = row[4]
	table.admin_name2 = row[5]
	table.admin_code2 = row[6]
	table.admin_name3 = row[7]
	table.admin_code3 = row[8]
	table.latitude = row[9]
	table.longitude = row[10]
	table.accuracy = row[11]
	try:
		table.save()
	except ValueError:
		print("Fail! " + row[2])
