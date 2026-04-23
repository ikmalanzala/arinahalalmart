from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produk/<int:id>/', views.detail_produk, name='detail_produk'),
    path('tentang/', views.tentang, name='tentang'),
    path('artikel/', views.artikel_list, name='artikel'),
    path('artikel/<slug:slug>/', views.artikel_detail, name='artikel_detail'),
]
