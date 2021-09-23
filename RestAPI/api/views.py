import re
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from rest_framework import response, serializers
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt

#1                                                                        FUNCTION METHOD API CHIQARISHI

@csrf_exempt #post qilishda majburiy qushish kk bulmasa 500
def article_list(request):
    if request.method  == "GET":
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many = True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def article_details(request,pk):
    try: 
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse('Mavjud emas')
    
    if  request.method  == "GET":
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
    elif  request.method  == "PUT":#update
        data = JSONParser().parse(request) 
        serializer = ArticleSerializer(article,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    elif  request.method  == "DELETE":
        article.delete()
        return HttpResponse(status=204)



#Don't repeat yourself
#2                                                                           api_view METHOD 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET',"POST"])
def article_list(request):
    if request.method  == "GET":
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many = True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',"PUT","DELETE"])
def article_details(request,pk):

    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status.HTTP_404_NOT_FOUND)
    
    if  request.method  == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif  request.method  == "PUT":#update
       
        serializer = ArticleSerializer(article,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif  request.method  == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#                                                           CLASS BASED API VIEW
from rest_framework.views import APIView
class APIViewCLASS(APIView):
    def get(self,request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Article_details(APIView):
    #id olib beradi
    def get_object(self,id):
        try:
            return Article.objects.get(id = id)
        except Article.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    
    def get(self,request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self,request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#                                                                GenericAPIView
#authercations
from rest_framework.authentication import BasicAuthentication, SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from rest_framework import mixins

class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin): #list , create,update
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'

    authentication_classes = [SessionAuthentication,BasicAuthentication] # 1->2 ... login register
    # authentication_classes = [TokenAuthentication] #token bulib kirish kerak buladi admin faqat
    permission_classes = [IsAuthenticated] #login bulish kerak

    #get method
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    #post method
    def post(self,request):
        return self.create(request)
    
    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self, request,id):
        return self.destroy(request, id)

#                                VIEWSET
from  rest_framework import viewsets
#modelviewset
class APIViewsset(viewsets.ModelViewSet):
    serializer_class= ArticleSerializer
    queryset=Article.objects.all()