from django.contrib import admin
from appart.models import RentUser, Location, Apartment, Feedback, Image, SaveAps


admin.site.register(Apartment)
admin.site.register(RentUser)
admin.site.register(Location)
admin.site.register(Feedback)
admin.site.register(Image)
admin.site.register(SaveAps)