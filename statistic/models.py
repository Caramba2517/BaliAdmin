from django.db import models
from appart.models import Apartment, Location


class CommonStatistic(models.Model):
    date = models.DateField(verbose_name='Date', unique=True, null=False)
    link = models.IntegerField(verbose_name='Followed by bot link', blank=True, null=True, default=0)
    cmd_start = models.IntegerField(verbose_name='Command Start', blank=True, null=True, default=0)
    start_register = models.IntegerField(verbose_name='Change language', blank=True, null=True, default=0)
    finish_register = models.IntegerField(verbose_name='Registration', blank=True, null=True, default=0)
    contact = models.IntegerField(verbose_name='Click on the contact button', blank=True, null=True, default=0)
    subscribe = models.IntegerField(verbose_name='Subscribed', blank=True, null=True, default=0)
    find = models.IntegerField(verbose_name='Started searching', blank=True, null=True, default=0)
    search = models.IntegerField(verbose_name='Started executing the request', blank=True, null=True, default=0)

    def __str__(self):
        return f'Date: {self.date}'


class ApartStatistic(models.Model):
    apart = models.OneToOneField(Apartment, verbose_name='Date upload and Unique ID apartment',
                                 on_delete=models.CASCADE,
                                 unique=True)
    views = models.IntegerField(verbose_name='Views', blank=True, null=True, default=0)
    favorite = models.IntegerField(verbose_name='Add to favorite', blank=True, null=True, default=0)
    contact = models.IntegerField(verbose_name='View agent contact', blank=True, null=True, default=0)
    find_date = models.DateTimeField(verbose_name='Last view in find', blank=True, null=True)
    favorite_date = models.DateTimeField(verbose_name='Last add in favorite', blank=True, null=True)

    def __str__(self):
        return f'{self.apart}'


class LocationStatistic(models.Model):
    date = models.DateField(verbose_name='Date')
    index = models.TextField(verbose_name='Location', blank=True, null=True)

    def __str__(self):
        return f'Date: {self.date}'


class PriceUSDStatistic(models.Model):
    date = models.DateField()
    first_month = models.IntegerField(verbose_name='[MONTH] Less than 650', blank=True, null=True, default=0)
    second_month = models.IntegerField(verbose_name='[MONTH] 650 - 1300$', blank=True, null=True, default=0)
    third_month = models.IntegerField(verbose_name='[MONTH] 1300 - 1950$', blank=True, null=True, default=0)
    fourth_month = models.IntegerField(verbose_name='[MONTH] 1950 - 2600$', blank=True, null=True, default=0)
    fifth_month = models.IntegerField(verbose_name='[MONTH] 2600 - 3250$', blank=True, null=True, default=0)
    sixth_month = models.IntegerField(verbose_name='[MONTH] more than 3250$', blank=True, null=True, default=0)
    first_day = models.IntegerField(verbose_name='[DAY] Less than 20$', blank=True, null=True, default=0)
    second_day = models.IntegerField(verbose_name='[DAY] 20 - 50$', blank=True, null=True, default=0)
    third_day = models.IntegerField(verbose_name='[DAY] 50 - 70$', blank=True, null=True, default=0)
    fourth_day = models.IntegerField(verbose_name='[DAY] 70 - 100$', blank=True, null=True, default=0)
    fifth_day = models.IntegerField(verbose_name='[DAY] 100 - 140$', blank=True, null=True, default=0)
    sixth_day = models.IntegerField(verbose_name='[DAY] More than 140$', blank=True, null=True, default=0)
    first_year = models.IntegerField(verbose_name='[YEAR] Less than 8000$', blank=True, null=True, default=0)
    second_year = models.IntegerField(verbose_name='[YEAR] 8000 - 16000$', blank=True, null=True, default=0)
    third_year = models.IntegerField(verbose_name='[YEAR] 16000 - 24000$', blank=True, null=True, default=0)
    fourth_year = models.IntegerField(verbose_name='[YEAR] 24000 - 32000$', blank=True, null=True, default=0)
    fifth_year = models.IntegerField(verbose_name='[YEAR] 32000 - 40000$', blank=True, null=True, default=0)
    sixth_year = models.IntegerField(verbose_name='[YEAR] More than 40000$', blank=True, null=True, default=0)

    def __str__(self):
        return f'Date: {self.date}'


class PriceRUPStatistic(models.Model):
    date = models.DateField()
    first_day = models.IntegerField(verbose_name='[DAY] Less than 300k', blank=True, null=True, default=0)
    second_day = models.IntegerField(verbose_name='[DAY] 300k - 700k', blank=True, null=True, default=0)
    third_day = models.IntegerField(verbose_name='[DAY] 700k - 1 mln', blank=True, null=True, default=0)
    fourth_day = models.IntegerField(verbose_name='[DAY] 1 mln - 1,5 mln', blank=True, null=True, default=0)
    fifth_day = models.IntegerField(verbose_name='[DAY] 1,5 mln - 2 mln', blank=True, null=True, default=0)
    sixth_day = models.IntegerField(verbose_name='[DAY] more than 2 mln', blank=True, null=True, default=0)
    first_month = models.IntegerField(verbose_name='[MONTH] less than 10 mln', blank=True, null=True, default=0)
    second_month = models.IntegerField(verbose_name='[MONTH] 10 mln - 20 mln', blank=True, null=True, default=0)
    third_month = models.IntegerField(verbose_name='[MONTH] 20 mln - 30 mln', blank=True, null=True, default=0)
    fourth_month = models.IntegerField(verbose_name='[MONTH] 30 mln - 40 mln', blank=True, null=True, default=0)
    fifth_month = models.IntegerField(verbose_name='[MONTH] 40 mln - 50 mln', blank=True, null=True, default=0)
    sixth_month = models.IntegerField(verbose_name='[MONTH] more than 50 mln', blank=True, null=True, default=0)
    first_year = models.IntegerField(verbose_name='[YEAR] less than 120 mln', blank=True, null=True, default=0)
    second_year = models.IntegerField(verbose_name='[YEAR] 120 mln - 240 mln', blank=True, null=True, default=0)
    third_year = models.IntegerField(verbose_name='[YEAR] 240 mln - 360 mln', blank=True, null=True, default=0)
    fourth_year = models.IntegerField(verbose_name='[YEAR] 360 mln - 480 mln', blank=True, null=True, default=0)
    fifth_year = models.IntegerField(verbose_name='[YEAR] 480 mln - 600 mln', blank=True, null=True, default=0)
    sixth_year = models.IntegerField(verbose_name='[YEAR] more than 600 mln', blank=True, null=True, default=0)

    def __str__(self):
        return f'Date: {self.date}'


class AdsStatistic(models.Model):
    date = models.DateField(verbose_name='Date', unique=True, null=False)
    daily = models.IntegerField(verbose_name='New ads per day', blank=True, null=True, default=0)
    total = models.IntegerField(verbose_name='All ads', blank=True, null=True, default=0)

    def __str__(self):
        return f'Date: {self.date}'

