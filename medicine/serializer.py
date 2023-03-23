from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from accounts.models import Peracik
from .models import Medicine
from ingredient.models import Ingredient
from ingredient.serializer import IngredientSerializer
from accounts.serializer import UserSerializer

local = 'http://127.0.0.1:8000'
deployment = 'https://deployailment.pythonanywhere.com'

def build_url(url):
    return f'{deployment}{url}'


class MedicineSerializer(serializers.ModelSerializer):
    
    ingredients = IngredientSerializer(many=True, required=True)
    description = serializers.CharField(required=True)
    peracik = serializers.StringRelatedField(read_only=True)
    usage_rules = serializers.CharField(required=True)
    ways_to_use = serializers.CharField(required=True)
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        try:
            return build_url(obj.image.url)
        except:
            return None
    
    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        if ingredients:
            for ingredient in ingredients:
                if not Ingredient.objects.filter(**ingredient).exists():
                    raise serializers.ValidationError('Ingredient not found')
        
        current_peracik = get_object_or_404(Peracik, user=self.context['request'].user)
        medicine= Medicine.objects.create(**validated_data, peracik=current_peracik)
        for ingredient in ingredients:
            ingredient = get_object_or_404(Ingredient, **ingredient)
            if ingredient not in medicine.ingredients.all():
                medicine.ingredients.add(ingredient)
                ingredient.medicine_many.add(medicine)

        return medicine
    
    class Meta:
        model = Medicine
        fields = ("id","name", "image", "description","status", "usage_rules", "ways_to_use", "peracik", "message_status","ingredients")

class DashboardPeracikSerializer(serializers.ModelSerializer):
    
    email = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    
    def get_email(self, obj):
        try :
            return obj.user.email
        except:
            return None
    
    def get_name(self, obj):
        try :
            return obj.user.username
        except:
            return None
    
    class Meta:
        model = Peracik
        fields = ("name", "email", "status", "message_status")
# nama obat
# image
# peracik
# description
# usage_rules
# ways of making
# status
# ingredients