from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from accounts.models import Peracik
from .models import Medicine
from ingredient.models import Ingredient
from ingredient.serializer import IngredientSerializer
from accounts.serializer import UserSerializer

class MedicineSerializer(serializers.ModelSerializer):
    
    ingredients = IngredientSerializer(many=True, required=True)
    description = serializers.CharField(required=True)
    peracik = serializers.StringRelatedField(read_only=True)
    usage_rules = serializers.CharField(required=True)
    ways_to_use = serializers.CharField(required=True)
    image = serializers.ImageField(required=False)
        
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

class PeracikDashboardSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    accepted_medicine = serializers.SerializerMethodField()
    pending_medicine = serializers.SerializerMethodField()
    canceled_medicine = serializers.SerializerMethodField()
    
    def get_profile(self, obj):
        return { "name": obj.user.username, "email": obj.user.email}
    
    def get_accepted_medicine(self, obj):
        return MedicineSerializer(Medicine.objects.filter(status='ACCEPTED'), many=True).data
    def get_pending_medicine(self, obj):
        return MedicineSerializer(Medicine.objects.filter(status='WAITING'), many=True).data
    def get_canceled_medicine(self, obj):
        return MedicineSerializer(Medicine.objects.filter(status='CANCELED'), many=True).data

    class Meta:
        model = Peracik
        fields = ("profile","accepted_medicine", "pending_medicine", "canceled_medicine")
# nama obat
# image
# peracik
# description
# usage_rules
# ways of making
# status
# ingredients