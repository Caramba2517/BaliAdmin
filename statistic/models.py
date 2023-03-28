from django.db import models
from appart.models import Apartment, Location


class CommonStatistic(models.Model):
    date = models.DateField(verbose_name='Date', unique=True, null=False)
    link = models.IntegerField(verbose_name='Followed by bot link', blank=True, null=True, default=0)
    cmd_start = models.IntegerField(verbose_name='Command Start', blank=True, null=True, default=0)
    start_register = models.IntegerField(verbose_name='Started registration', blank=True, null=True, default=0)
    finish_register = models.IntegerField(verbose_name='Finished registration', blank=True, null=True, default=0)
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
    first = models.IntegerField(verbose_name='Less than 650', blank=True, null=True, default=0)
    second = models.IntegerField(verbose_name='650 - 1300$', blank=True, null=True, default=0)
    third = models.IntegerField(verbose_name='1300 - 1950$', blank=True, null=True, default=0)
    fourth = models.IntegerField(verbose_name='1950 - 2600$', blank=True, null=True, default=0)
    fifth = models.IntegerField(verbose_name='2600 - 3250$', blank=True, null=True, default=0)
    sixth = models.IntegerField(verbose_name='more than 3250$', blank=True, null=True, default=0)

    def __str__(self):
        return f'Date: {self.date}'


class PriceRUPStatistic(models.Model):
    date = models.DateField()
    first = models.IntegerField(verbose_name='less than 10 mln', blank=True, null=True, default=0)
    second = models.IntegerField(verbose_name='10 mln - 20 mln', blank=True, null=True, default=0)
    third = models.IntegerField(verbose_name='20 mln - 30 mln', blank=True, null=True, default=0)
    fourth = models.IntegerField(verbose_name='30 mln - 40 mln', blank=True, null=True, default=0)
    fifth = models.IntegerField(verbose_name='40 mln - 50 mln', blank=True, null=True, default=0)
    sixth = models.IntegerField(verbose_name='more than 50 mln', blank=True, null=True, default=0)

    def __str__(self):
        return f'Date: {self.date}'


class AdsStatistic(models.Model):
    date = models.DateField(verbose_name='Date', unique=True, null=False)
    daily = models.IntegerField(verbose_name='New ads per day', blank=True, null=True, default=0)
    total = models.IntegerField(verbose_name='All ads', blank=True, null=True, default=0)

    def __str__(self):
        return f'Date: {self.date}'
