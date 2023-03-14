from django.db import models

# Create your models here.


class Statistic(models.Model):
    date = models.DateTimeField(verbose_name='Date', unique=True, null=False)
    unique_users = models.IntegerField(verbose_name='Unique Users', blank=True, null=True)
    users_start = models.IntegerField(verbose_name='Command Start', blank=True, null=True)
    users_finsh = models.IntegerField(verbose_name='Communication with an agent', blank=True, null=True)
    users_pay = models.IntegerField(verbose_name='Made a payment', blank=True, null=True)

    def __str__(self):
        return f'Date: {self.date}'
