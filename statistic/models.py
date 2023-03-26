from django.db import models

# Create your models here.

class UsersStatistic(models.Model):
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
