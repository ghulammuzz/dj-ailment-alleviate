from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Bahan
from .serialiezer import *

class DashboardView(viewsets.ModelViewSet):
    queryset = Obat.objects.all()
    
    permission_classes = [AllowAny]
    serializer_class = ObatSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nama_Obat']
    
    def get(self, request):
        bahan = Obat.objects.all()
        serializer = ObatSerializer(bahan, many=True)
        return Response(serializer.data)