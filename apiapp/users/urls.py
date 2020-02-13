
from django.urls import path

from .views import LoginView

urlpatterns = [
    path('auth/users/login', LoginView.as_view(), name='user_login'),
    #path('auth/users/login', ),
]
