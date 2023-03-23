from rest_framework import serializers
from ingredient.models import Ingredient

from ingredient.serializer import IngredientSerializer
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']
        

class CategoryWithIngredientsSerializer(serializers.ModelSerializer):
    # ingredient = IngredientSerializer(many=True,read_only=True)
    ingredient = serializers.SerializerMethodField()
    
    def get_ingredient(self, obj):
        list = []
        ingredients = Ingredient.objects.filter(category=obj)
        for ingredient in ingredients:
            list.append(IngredientSerializer(ingredient).data)
        return list

    class Meta:
        model = Category
        fields = ['name', 'description', 'ingredient']
