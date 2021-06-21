from django.urls import path
from App_Admin import views

app_name = 'App_Admin'

urlpatterns = [
    path('master',views.master,name='master'),
    path('adminhome',views.AdminHome,name='adminhome'),
    path('organizations',views.organizations,name='organizations'),
    path('verifiedusers',views.verifiedusers,name='verifiedusers'),
    path('generalusers',views.generalusers,name='generalusers'),
    path('eventsbyusers',views.eventsbyusers,name='eventsbyusers'),
    path('eventsbyorganizations',views.eventsbyorganizations,name='eventsbyorganizations'),
]
