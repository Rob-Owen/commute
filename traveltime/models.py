from django.db import models

# UK locations, modified from Becca's USA work
class UK_locations(models.Model):
	country_code = models.CharField(max_length=2)
	postal_code = models.CharField(max_length=20)
	place_name = models.CharField(max_length=180, db_index=True)
	admin_name1 = models.CharField(max_length=100)
	admin_code1 = models.CharField(max_length=20)
	admin_name2 = models.CharField(max_length=100)
	admin_code2 = models.CharField(max_length=20)
	admin_name3 = models.CharField(max_length=100)
	admin_code3 = models.CharField(max_length=20)
	latitude = models.FloatField()
	longitude = models.FloatField()
	accuracy = models.IntegerField()

# UK town populations ()
class Population(models.Model):
	place_name = models.CharField(max_length=180, db_index=True)
	pop = models.IntegerField()