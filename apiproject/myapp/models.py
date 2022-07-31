from django.db import models
from django.db import models
from rest_framework import serializers
from datetime import datetime, date
from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Birth_year = models.IntegerField(default=2022)
    age = models.IntegerField(default=0)


    def save(self, *args, **kwargs):
        if self.Birth_year > date.today().year:
            raise ValidationError("Birth year cannot be in the future!")
        super(Contact, self).save(*args, **kwargs)

    @property
    def age(self):
        today = date.today()
        birth = self.Birth_year
        newage = today.year - birth
        return newage

    def __str__(self):
        return self.Name











# Create your models here.
