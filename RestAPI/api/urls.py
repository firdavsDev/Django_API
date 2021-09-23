from django.db import router
from django.urls import path,include

from .views import APIViewCLASS,Article_details,GenericAPIView,article_list,article_details,APIViewsset
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('viewsset',APIViewsset,basename='Article')

urlpatterns = [
    
    path('accounts/', include('rest_framework.urls')),
#functionMethod
    # path('articles/',article_list,name="Article_list"),
    # path('article_detail/<int:pk>',article_details,name="Article_list"),
#classMethod
    path('articles/',APIViewCLASS.as_view(),name="Article_APIClass"),
    path('article_detail/<int:id>',Article_details.as_view(),name="Article_list"),
#generic method
    path('generic/',GenericAPIView.as_view(),name="Article_APIClass"),
    path('generic/<int:id>/',GenericAPIView.as_view(),name="Article_APIClass"),
    #viewset
    path('viewset/',APIViewsset.as_view({'get': 'list','post':'create'})),
    path('viewsset/',include(router.urls)),
]

