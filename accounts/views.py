from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import *
from .serializer import *
from .tokens import create_jwt_pair_for_user
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

class PeracikLoginView(generics.GenericAPIView):
    serializer_class = PeracikLoginSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializers = self.get_serializer(data=request.data)
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(email=email, password=password)
        if User.objects.filter(is_peracik=True, email=email).exists() and user is not None:
            token = create_jwt_pair_for_user(user)
            return Response({"pesan":"Berhasil login", "token":token})
        return Response({"pesan":"Gagal login"})