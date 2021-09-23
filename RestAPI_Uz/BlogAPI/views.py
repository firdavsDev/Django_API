from django.shortcuts import render

# Create your views here.
from .models import Post  #modellarimiz
from .serializers import PostSerializer,UserSerialeser #serialasers

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView #apiview
from rest_framework import permissions #ruxsatlar

from .permissions import IsAuthorOrReadOnly #file
from django.contrib.auth import get_user_model

class Postlist(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
   
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#33333333333333333333333333333333333333333333333333333333333333333333 User uchun
class UserList(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerialeser

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerialeser



################################################################# Viewsetda ishlash
from rest_framework.viewsets import ModelViewSet
class PostViewset(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewset(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerialeser