from django.contrib import admin
from statistic.models import CommonStatistic, ApartStatistic, AdsStatistic, LocationStatistic, PriceRUPStatistic, PriceUSDStatistic
# Register your models here.


admin.site.register(CommonStatistic)
admin.site.register(ApartStatistic)
admin.site.register(AdsStatistic)
admin.site.register(LocationStatistic)
admin.site.register(PriceUSDStatistic)
admin.site.register(PriceRUPStatistic)