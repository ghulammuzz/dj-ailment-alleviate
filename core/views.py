from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from .models import Bahan
from .serialiezer import *

# class BahanFilter(filters.FilterSet):
    
#     class Meta:
#         model = Obat
#         fields = ['bahan']

class DashboardView(generics.ListAPIView, viewsets.ModelViewSet):
    queryset = Obat.objects.all()
    
    permission_classes = [AllowAny]
    serializer_class = ObatSerializer
    filter_backends = [SearchFilter]
    # filterset_class = BahanFilter
    search_fields = [
        'nama_obat',
        'bahan_1__nama_bahan',
        'bahan_2__nama_bahan',
        'bahan_3__nama_bahan',
        'bahan_4__nama_bahan',
        'bahan_5__nama_bahan',
        'bahan_6__nama_bahan',
        'bahan_7__nama_bahan',
        ]
    
    def get(self, request):
        bahan = Obat.objects.all()
        serializer = ObatSerializer(bahan, many=True)
        return Response({
            "obat": serializer.data,
        })