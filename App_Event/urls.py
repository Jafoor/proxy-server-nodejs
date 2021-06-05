from django.urls import path
from App_Event import views

app_name = 'App_Event'

urlpatterns = [
    path('', views.Home, name='home'),
    # path('product/<pk>/', views.ProductDetail.as_view(), name='product_detail'),
]
