from rest_framework import serializers
from .models import Ingredient

local = 'http://127.0.0.1:8000'
deployment = 'https://deployailment.pythonanywhere.com'

def build_url(url):
    return f'{deployment}{url}'

class IngredientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.StringRelatedField(read_only=True) 
    image = serializers.SerializerMethodField() 
    # medicine_many = serializers.StringRelatedField(many=True, read_only=True)
    
    def get_image(self, obj):
        try:
            return build_url(obj.image.url)
        except:
            return None 
    
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'image', 'status', 'category']