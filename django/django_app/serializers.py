from rest_framework import serializers
from django_app import models


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Model
        fields = "__all__"
