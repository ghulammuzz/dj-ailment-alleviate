from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Bahan
from .serialiezer import *
# Create your views here.

class DashboardView(viewsets.ModelViewSet):
    queryset = Penyakit.objects.all()
    
    permission_classes = [AllowAny]
    serializer_class = PenyakitSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nama_penyakit']
    
    def get(self, request):
        bahan = Penyakit.objects.all()
        serializer = PenyakitSerializer(bahan, many=True)
        return Response(serializer.data)