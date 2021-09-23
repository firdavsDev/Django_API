from rest_framework import fields, serializers
from .models import Post
#modeldagi malumotlarni json kurinshga uzgartirish
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ['id','title','descrption']#'__all__'
        fields = '__all__'
        
class UserSerialeser(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id","username")