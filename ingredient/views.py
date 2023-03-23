from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Ingredient
from .serializer import IngredientSerializer
# Create your views here.

class ListIngredient(generics.ListCreateAPIView, generics.GenericAPIView, mixins.RetrieveModelMixin):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'category__name']
    permission_classes = []
    
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)