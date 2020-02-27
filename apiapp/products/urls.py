from django.urls import path
from .views import ProductsView
from .views import ProductsList
from .views import CategoryView
from .views import CategoryList

urlpatterns = [
    path('<int:pk>', ProductsList.as_view(), name='add_product'),
    path('', ProductsView.as_view(), name='view_product'),
    path('category/<int:pk>', CategoryList.as_view(), name='add_category'),
    path('category/', CategoryView.as_view(), name='view_category'),
]
