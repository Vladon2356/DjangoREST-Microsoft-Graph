from django.contrib import admin
from django.urls import path, include
from core.yasg import urlpatterns as doc_urls

from apps.api.views import GetAccessTockenAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('microsoft/auth-callback/', GetAccessTockenAPIView.as_view(), name='get-access-token'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/', include('apps.api.urls', namespace='api')),
]
urlpatterns += doc_urls
