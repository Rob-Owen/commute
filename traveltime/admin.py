from django.contrib import admin

from .models import uk_location, Population, DistanceMatrix, LargeTown

admin.site.register(uk_location)
admin.site.register(Population)
admin.site.register(DistanceMatrix)
admin.site.register(LargeTown)