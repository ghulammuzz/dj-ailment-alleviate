from rest_framework import generics
from .models import Category
from .serializer import CategorySerializer

# Create your views here.

class ListCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer