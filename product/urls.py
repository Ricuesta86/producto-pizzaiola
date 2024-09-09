from django.urls import path
from . import views


urlpatterns = [
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('',views.home,name="home"),
    # Products
    path('products/',views.products, name='products'),
    path('products/new/',views.new_product, name='products_new'),
    path('products/<int:id>/update/', views.update_product, name='products_update'),
    path('products/<int:id>/detail/', views.detail_product, name='products_detail'),
    path('products/<int:id>/delete/', views.delete_product, name='products_delete'),
    path('products/<int:id>/pdf/', views.generar_pdf_product, name='products_pdf'),
    path('exportar-excel/', views.export_to_excel, name='export_to_excel'),
    # Agregados
    path('products/<int:producto_id>/aggregate/new/', views.new_aggregate, name='aggregate_new'),
    path('products/<int:producto_id>/aggregate/<int:id>/delete/', views.delete_aggregate, name='aggregate_delete'),
    # path('aggregate/<int:id>/update/', views.update_aggregate, name='aggregate_update'),
    # path('aggregate/<int:id>/delete/', views.delete_aggregate, name='aggregate_delete'),
]