from rest_framework import serializers
from .models import Contact
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from django.db import transaction

class ContactSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(max_length=100)
    Birth_year = serializers.IntegerField(default=2022)
    #age = serializers.SerializerMethodField()


    #def get_age(self, datetime):return relativedelta(self.Birthdate.days, datetime.date.now()).years

    class Meta:
        model = Contact
        fields = ('Name','Birth_year','age')

    def to_representation(self, instance):
        response = {
            "set_attributes" : super().to_representation(instance),
        }
        return response


class ListingSerializer(serializers.ModelSerializer):
    age = serializers.Field(source='age')

















