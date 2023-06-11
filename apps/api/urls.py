from django.urls import path

from apps.api import views

app_name = 'api'

urlpatterns = [
    path('get-auth-url/', views.GetAuthURL.as_view(), name='get-auth-url'),
    path('get-user-data/', views.GetUserInfoAPIView.as_view(), name='get-user-data'),
    path('get-access-token/', views.GetAccessTockenAPIView.as_view(), name='get-access-token'),
    path('send-email/', views.SendEmaiAPIView.as_view(), name='send-email'),
]