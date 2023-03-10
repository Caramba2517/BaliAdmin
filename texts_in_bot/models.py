from django.db import models


# Create your models here.

class Text(models.Model):
    action = models.IntegerField(unique=True, null=False)
    text_in_russian = models.TextField(null=False)
    text_in_english = models.TextField(null=False)
    text_in_indonesian = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Action: {self.action}, English: {self.text_in_english}'
