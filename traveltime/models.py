from django.db import models

# UK locations, modified from Becca's USA work
class uk_location(models.Model):
	country_code = models.CharField(max_length=2)
	postal_code = models.CharField(max_length=20)
	place_name = models.CharField(max_length=180, primary_key=True)
	admin_name1 = models.CharField(max_length=100, null=True)
	admin_code1 = models.CharField(max_length=20, null=True)
	admin_name2 = models.CharField(max_length=100, null=True)
	admin_code2 = models.CharField(max_length=20, null=True)
	admin_name3 = models.CharField(max_length=100, null=True)
	admin_code3 = models.CharField(max_length=20, null=True)
	latitude = models.FloatField()
	longitude = models.FloatField()
	accuracy = models.IntegerField(null=True)

	def __str__(self):
		return "%s (%s)" % (self.place_name, self.admin_name2)

# UK town populations ()
class Population(models.Model):
	place_name = models.CharField(max_length=180, db_index=True)
	region_name = models.CharField(max_length=100, null=True) # e.g. city
	pop = models.IntegerField()

	location = models.ForeignKey( 'uk_location', on_delete = models.SET_NULL,
								  related_name = 'pop_entry', null=True)

	def __str__(self):
		return "%s: %i" % (self.place_name, self.pop)


class DistanceMatrix+(models.Model):
	linear_distance = models.IntegerField()

	def __str__(self):
		return "%s --> %s: %s miles" % (self.place1, self.place2, self.linear_distance)

class LargeTown(models.Model):
	place_name = models.CharField(max_length=180, primary_key=True)
	admin_name1 = models.CharField(max_length=100, null=True)
	admin_name2 = models.CharField(max_length=100, null=True)
	admin_name3 = models.CharField(max_length=100, null=True)
	latitude = models.FloatField()
	longitude = models.FloatField()
	pop = models.IntegerField()

	route_starts = models.ForeignKey( 'DistanceMatrix', on_delete=models.SET_NULL,
									   related_name='place1', null=True)
	route_ends = models.ForeignKey( 'DistanceMatrix', on_delete=models.SET_NULL,
									   related_name='place2', null=True)

	def __str__(self):
		return "%s (%s)" % (self.place_name, self.pop)