from django.urls import path
from App_Admin import views

app_name = 'App_Admin'

urlpatterns = [
    # path('master',views.master,name='master'),
    path('dashboard/home',views.Home,name='adminhome'),
    path('dashboard/organizationlist',views.Organizationlist,name='organizationlist'),
    path('dashboard/eventlist', views.Eventlist,name='eventlist'),
    path('dashboard/notverifiedeventlist', views.UnverifiedEventlist,name='notverifiedeventlist'),
    path('dashboard/allusers', views.AllUsers,name='allusers'),
    # path('verifiedusers',views.verifiedusers,name='verifiedusers'),
    # path('generalusers',views.generalusers,name='generalusers'),
    # path('eventsbyusers',views.eventsbyusers,name='eventsbyusers'),
    # path('eventsbyorganizations',views.eventsbyorganizations,name='eventsbyorganizations'),
]
