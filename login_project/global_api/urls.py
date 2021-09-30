from django.urls import path
from .views import CreateUser,UserLogin

urlpatterns = [

    path('global_api/login', UserLogin.as_view(), name='login_api'),
    path('global_api/register', CreateUser.as_view(), name='register_api'),
]