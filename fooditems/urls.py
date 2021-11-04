from django.urls import path
from . import views

urlpatterns = [
    path('', views.items, name='items'),
    path('<int:item_id>/', views.single, name='single'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_cart/<int:id>/',views.update_cart, name='update_cart'),
]