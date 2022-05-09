from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import routers
from . import views

app_name = 'accounts'
router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += router.urls

# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1MjE1OTEzNywiaWF0IjoxNjUyMDcyNzM3LCJqdGkiOiJmODNlZGFmNjA1MDU0ODk0OGQ0ZTY1MjUyMzMzMGM4NiIsInVzZXJfaWQiOjF9.1wWu0IKZQ_BJydh0Sw8QPfDgKXL4fsYB6j6s2gOhcyI",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMDczMDM3LCJpYXQiOjE2NTIwNzI3MzcsImp0aSI6IjhmOWFkYmNjZjM2MjRmZTE4ODRmYTQ0ZmU2YmQxYzM3IiwidXNlcl9pZCI6MX0.WASi9767ZL33zP6VJY2DbleZNmciBZIwATUrNvcc7oY"
# }