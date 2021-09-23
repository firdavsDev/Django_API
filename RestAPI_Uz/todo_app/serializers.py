from rest_framework import serializers
from .models import ToDo
#modeldagi malumotlarni json kurinshga uzgartirish

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id','title','descrption']#'__all__'
        # fields = '__all__'
        
