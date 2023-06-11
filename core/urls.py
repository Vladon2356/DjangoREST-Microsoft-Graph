from django.contrib import admin
from django.urls import path, include
from core.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/', include('apps.api.urls', namespace='api')),
]
urlpatterns += doc_urls
