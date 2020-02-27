from django.urls import path
from .views import ProductsView
from .views import ProductsList

urlpatterns = [
    path('<int:pk>', ProductsList.as_view(), name='add_product'),
    path('', ProductsView.as_view(), name='add_product'),
]
