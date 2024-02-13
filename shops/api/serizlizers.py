from rest_framework import serializers
from visits.models import Store, Visit


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ("id", "title")


class VisitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ("store", "latitude", "longitude")


class VisitResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ("id", "visit_date")
