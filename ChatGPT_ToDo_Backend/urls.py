from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', obtain_auth_token, name='api_token_auth'),
    path('api/register/', RegisterUserView.as_view(), name='api_register'),
    path('api/', include('todos.urls')),
]
