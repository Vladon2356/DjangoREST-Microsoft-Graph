from django.urls import path

from apps.api import views

app_name = 'api'

urlpatterns = [
    path('get-auth-url/', views.GetAuthURL.as_view(), name='get-auth-url'),
    path('get-access-token/', views.GetAccessTockenAPIView.as_view(), name='get-access-token'),
]