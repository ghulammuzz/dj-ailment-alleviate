from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from ingredient.models import Ingredient
from .models import Category
from .serializer import CategoryWithIngredientsSerializer

# Create your views here.

class ListCategory(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategoryWithIngredientsSerializer
    queryset = Category.objects.all()
