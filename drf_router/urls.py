from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework import routers
# from rest_framework.authentication.views import obtain_auth_token


router = DefaultRouter()
router.register(r'api/users', UserViewset, basename="user_mgt")


urlpatterns = [
    path(r'', include(router.urls)),
    path(r'rest/', include('rest_framework.urls')),
    path('api/post/users/', UserCreateAPIView.as_view()),
    path('api/ud/', CreateUserDetails.as_view()),   #OneToOne
]