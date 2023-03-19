from rest_framework.response import Response
from rest_framework import generics, viewsets, mixins
from annoying.functions import get_object_or_None
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from accounts.models import *
from accounts.serializer import *
from .models import *
from .serialiezer import *

class DashboardView(
    generics.ListAPIView,
    generics.GenericAPIView,
    mixins.RetrieveModelMixin
    ):
    
    fields = []
    fields.append('nama_obat')
    for i in range(1,8):
        fields.append(f'bahan_{i}__nama_bahan')
    
    queryset = Obat.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ObatSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = fields
    
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)
        
class BahanView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin
    ):
    
    queryset = Bahan.objects.all()
    permission_classes = [AllowAny]
    serializer_class = BahanSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nama_bahan']
    
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

class DashboardPeracikView(
    generics.GenericAPIView,
    ):
    
    queryset = Obat.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ObatSerializer
    
    def get(self, request, pk=None):
        current_user = request.user
        user = Peracik.objects.get(user=request.user)
        serializer_profile = HomePeracikSerializer(user).data
        
        if Peracik.objects.filter(user=current_user, status='MENUNGGU'):
            return Response(
                {
                    "pesan":"Akun anda belum dikonfirmasi oleh admin",
                    "status":"MENUNGGU"}
                , status=200)
        elif Peracik.objects.filter(user=current_user, status='DITOLAK'):
            return Response({"pesan":"Akun anda ditolak oleh admin","status":"DITOLAK"}, status=200)
        elif Peracik.objects.filter(user=current_user, status='DITERIMA'):
            pending = Obat.objects.filter(peracik__user=current_user, status='MENUNGGU')
            accepted = Obat.objects.filter(peracik__user=current_user, status='DITERIMA')
            pending_data = ObatSerializer(pending, many=True).data
            accepted_data = ObatSerializer(accepted, many=True).data
            return Response(
                {
                    "profile" : serializer_profile,
                    "pending" : pending_data,
                    "accepted" : accepted_data,
                }
            )

class BuatObatView(
    generics.GenericAPIView,
    ):

    queryset = Obat.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ObatSerializer

    def post(self, request):
        current_user = request.user
        if Peracik.objects.filter(user=current_user, status='DITERIMA'):
            data_obat = Obat.objects.create(
                nama_obat=request.data['nama_obat'],
                peracik = get_object_or_404(Peracik, user=current_user),
                keterangan=request.data['keterangan'],
                aturan_pemakaian=request.data['aturan_pemakaian'],
                cara_pembuatan=request.data['cara_pembuatan'],
                gambar=request.data.get('gambar', 'obat/default.jpeg'),
                status='MENUNGGU',
                bahan_1 = get_object_or_None(Bahan, id=request.data.get('bahan_1', None)),
                bahan_2 = get_object_or_None(Bahan, id=request.data.get('bahan_2', None)),
                bahan_3 = get_object_or_None(Bahan, id=request.data.get('bahan_3', None)),
                bahan_4 = get_object_or_None(Bahan, id=request.data.get('bahan_4', None)),
                bahan_5 = get_object_or_None(Bahan, id=request.data.get('bahan_5', None)),
                bahan_6 = get_object_or_None(Bahan, id=request.data.get('bahan_6', None)),
                bahan_7 = get_object_or_None(Bahan, id=request.data.get('bahan_7', None)),
            )
            data_obat.save()
            return Response({"pesan":"Menunggu Konfirmasi dari admin"}, status=201)
        else :
            return Response({"pesan":"Akun anda belum diterima oleh admin"}, status=400)

class TambahBahanView(
    generics.GenericAPIView,
    ):
    queryset = Bahan.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BahanSerializer
    
    def post(self, request):
        current_user = request.user
        if Peracik.objects.filter(user=current_user, status='DITERIMA'):
            data_bahan = Bahan.objects.create(
                nama_bahan=request.data['nama_bahan'],
                keterangan=request.data['keterangan'],
                gambar=request.data.get('gambar', 'bahan/default.jpeg'),
                status='MENUNGGU',
            )
            data_bahan.save()
            return Response({"pesan":"Menunggu Konfirmasi dari admin"}, status=201)
        else :
            return Response({"pesan":"Akun anda belum diterima oleh admin"}, status=400)

class CategoryWithBahan(generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    
    def get(self, request):
        serializer = CategorySerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=200)
    
