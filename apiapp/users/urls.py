
from django.urls import path

from .views import LoginView
from .views import UserCreate
from users import views

urlpatterns = [
    path('auth/users/login/', LoginView.as_view(), name='user_login'),
    path('auth/users/', UserCreate.as_view(), name='user_create'),
    path('auth/users/req/', views.req)
]
