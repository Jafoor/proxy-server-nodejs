from django.urls import path
from App_Event import views

app_name = 'App_Event'

urlpatterns = [
    path('', views.Home, name='home'),
    path('contactus', views.Contactus, name='contactus'),
    path('eventdetails', views.Eventdetails, name='eventdetails'),
    path('organization/<slug:slug>/createevent', views.OrgApplyevent, name='organizationapplyforevent'),
    path('organization/<slug:slug>/eventlist', views.OrgEventList, name='organizationeventlist')
    # path('product/<pk>/', views.ProductDetail.as_view(), name='product_detail'),
]
