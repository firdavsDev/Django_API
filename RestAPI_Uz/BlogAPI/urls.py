from django.db import router
from django.urls import path,include
from .views import PostDetail,Postlist,UserDetail,UserList,PostViewset,UserViewset

#routers viewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("users",UserViewset,basename='users')
router.register('',PostViewset,basename='posts')

#schema 

# from rest_framework.schemas import get_schema_view #schima va dokumentla
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#dokumitatsiya
schema_view = get_schema_view(
    openapi.Info(
        title='Blog API',
        description="DRF lessonslar uz",
        default_version='v1',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email="xackercoder@gmail.com"),
        license=openapi.License(name='Blog api litsinsuyasi')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('posts/',Postlist.as_view(),name='Posts'),
    path('posts/<int:pk>/',PostDetail.as_view(),name='Post_id'),

    path('api-auth/', include('rest_framework.urls')),
    
    path('users/',UserList.as_view(),name='Users'),
    path('users/<int:pk>/',UserDetail.as_view(),name='User_id'),

    #dynamic uzgaruvchan
    # path('openapi/',get_schema_view(
    #     title='Blog Api',
    #     description='Django rest fremvorki uzbek tilida',
    #     version='1.0.0'
    # ),name='open_api')

    path('swagger/',schema_view.with_ui(
        'swagger',cache_timeout=0
    ),name='swagger-schema'),

    path('redoc/',schema_view.with_ui(
        'redoc',cache_timeout=0
    ),name='redoc-schema'),
]
urlpatterns += router.urls