from django.conf.urls import url
from django.urls import path

from .views import (
        LoginView,
        UserCreate,
        EmailActivateView,
        VendorCreate,
    )
from users import views

urlpatterns = [
    path('auth/users/login/', LoginView.as_view(), name='user_login'),
    path('auth/users/', UserCreate.as_view(), name='user_create'),
    path('auth/vendors/', VendorCreate.as_view(), name='vendor_create'),
    url(r'^auth/email/confirm/(?P<key>[0-9A-Za-z]+)/$', EmailActivateView.as_view(), name='email-activate'),
    #path('auth/users/req/', views.req)
]
