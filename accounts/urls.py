from django.urls import path
from rest_framework.authtoken import views as authtoken_views

from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('api-token-auth/', authtoken_views.obtain_auth_token)
]
