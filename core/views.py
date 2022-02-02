from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *

# Create your views here.
class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all().order_by('id')
    serializer_class = NewsSerializer
    permission_classes = [permissions.AllowAny]