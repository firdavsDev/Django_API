
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import ToDo
from .serializers import ToDoSerializer

class ListToDo(ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DetailToDo(RetrieveAPIView):

    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer