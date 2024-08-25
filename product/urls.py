from django.urls import path
from . import views


urlpatterns = [
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('',views.home,name="home"),
    path('products/',views.products, name='products'),
    path('products/new/',views.new_product, name='products_new'),
    path('products/<int:id>/update/', views.update_product, name='products_update'),
]