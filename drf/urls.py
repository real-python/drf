from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    # DRF 3rd Party Token Craetion 
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),

    # swagger custom response
    path('create/users/', CreateUSer.as_view()),

    # generics example
    path('api/users/', UserListCreateAPIView.as_view()),
    path('api/filter1/', FilterUser1.as_view()),
    path('api/filter2/<str:name>/', FilterUser2.as_view()),
    path('api/filter3/', FilterUser3.as_view()),
    path('api/filter4/', FilterUser4.as_view()),

    # FK realtion
    path('api/students/', StudentListView.as_view()),
    path('api/musicians/', MusicianListView.as_view()),
    path('api/albums/', AlbumListView.as_view()),

    # ManyToMany
    path('api/post/', PostCreateAPIView.as_view()),


]