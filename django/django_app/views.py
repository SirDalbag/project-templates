from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import render
from django_app import models, serializers


def index(request):
    return render(request, "index.html")


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def api(request):
    return Response(data={"message": "OK"})


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def get(request):
    objects = serializers.ModelSerializer(models.Model.objects.all(), many=True).data
    return Response(data={"message": objects})
