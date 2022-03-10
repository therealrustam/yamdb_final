from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API Yamdb",
        default_version='v1',
        description="Документация для приложения проекта API Yamdb",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(
        'redoc/', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]
