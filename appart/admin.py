from django.contrib import admin
from appart.models import RentUser, Location, Apartment, Feedback
# Register your models here.

admin.site.register(RentUser)
admin.site.register(Location)
admin.site.register(Apartment)
admin.site.register(Feedback)