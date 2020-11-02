from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Usr, Hunting, Cat
        
class HuntingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hunting
        fields = ['cat_id', 'prey_id', 'duration']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        
class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['cat_name', 'color_id', 'gender']