from geopy.distance import vincenty
import sys
import os
your_djangoproject_home="./commute"
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()

from traveltime.models import Population, uk_location, DistanceMatrix

done = []
for p1 in Population.objects.all():
	print(p1.place_name)
	for p2 in Population.objects.all():
		if {p1.place_name, p2.place_name} not in done:
			if p1.location is None or p2.location is None:
				continue
			origin = (float(p1.location.latitude), float(p1.location.longitude))
			dest = (float(p2.location.latitude), float(p2.location.longitude))
			dist = vincenty(origin, dest).miles
			n = DistanceMatrix( linear_distance=dist )
			n.save()
			p1.route_starts = n
			p2.route_ends = n
			p1.save()
			p2.save()
			done.append({p1.place_name, p2.place_name})
			#print("%s to %s:\t%d miles" % (p1.place_name, p2.place_name, dist))


"""
# Full path and name to your csv file
csv_filepathname="/Users/rebeccamorgan/Drive/Development/commute/GB.txt"
reader = csv.reader(open(csv_filepathname), delimiter='\t', quotechar='"')

# Count rows in file
row_count = sum(1 for row in reader)
origin_row = 0

# Prepare output file
with open('dists.csv', 'w') as csvoutfile:
	writer = csv.writer(csvoutfile, delimiter='\t', quotechar='"')
	
	for _ in range(row_count):
		# Restart reader and iterators
		reader = csv.reader(open(csv_filepathname), delimiter='\t', quotechar='"')
		row_iter = 0
		origin_row_iter = 0

		for row in reader:
			# Keep reading until you get to next origin
			if origin_row_iter >= origin_row:
				# Set origin
				if row_iter == 0:
					origin_name = row[2]
					origin_latitude = row[9]
					origin_longitude = row[10]
					origin = (float(origin_latitude), float(origin_longitude))
				else:
					# Loop through all possible destinations
					dest_name = row[2]
					dest_latitude = row[9]
					dest_longitude = row[10]
					dest = (float(dest_latitude), float(dest_longitude))

					# Calculate distance
					dist = vincenty(origin, dest).miles

					# Write to csv
					writer.writerow([origin_name, dest_name, dist])

				row_iter += 1

			origin_row_iter += 1

		origin_row += 1
"""