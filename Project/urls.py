# Django
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

# DRF
from rest_framework import permissions

# swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="PyWorld API",
      default_version='v 0.1',
      description="API documentation with Swagger",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   # Default Admin URL
   path('admin/', admin.site.urls),
   path('accounts/', include('django.contrib.auth.urls')),
   path('change-password/', auth_views.PasswordChangeView.as_view()),

   # SWagger URL
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   # App URL
   path('', include('drf.urls')),
   path('v1/', include('drf_router.urls')),

]
