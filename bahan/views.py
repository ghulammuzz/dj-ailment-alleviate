from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics

from .models import Bahan
from .serialiezer import *
# Create your views here.

class DashboardView(generics.GenericAPIView):
    
    queryset = Penyakit.objects.all()
    
    def get(self, request):
        bahan = Penyakit.objects.all()
        serializer = PenyakitSerializer(bahan, many=True)
        return Response(serializer.data)