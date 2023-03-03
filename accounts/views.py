from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import *
from .serializer import *
# Create your views here.

class PeracikSignUpView(generics.GenericAPIView):
    serializer_class = PeracikSignUpSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializers = self.get_serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"pesan":"Berhasil mendaftar"})
        return Response({"pesan":"Gagal mendaftar"})