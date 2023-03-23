from rest_framework import serializers
from .models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)  
    # medicine_many = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'image', 'status', 'category']