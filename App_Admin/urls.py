from django.urls import path
from App_Admin import views

app_name = 'App_Admin'

urlpatterns = [
    # path('master',views.master,name='master'),
    path('dashboard/home',views.Home,name='adminhome'),
    path('dashboard/organizationlist',views.Organizationlist,name='organizationlist'),
    path('dashboard/bannedorganizationlist',views.BannedOrganizationlist,name='bannedorganizationlist'),
    path('dashboard/unverifiedrganizationlist',views.UnverifiedOrganizationlist,name='unverifiedrganizationlist'),
    path('dashboard/organizationdetails/<slug:slug>',views.OrganizationDetails,name='organizationdetails'),
    path('dashboard/eventlist', views.Eventlist,name='eventlist'),
    path('dashboard/eventdetails/<slug:slug>', views.EventDetails,name='eventdetails'),
    path('dashboard/notverifiedeventlist', views.UnverifiedEventlist,name='notverifiedeventlist'),
    path('dashboard/allusers', views.AllUsers,name='allusers'),
    path('dashboard/verifiedusers', views.VerifiedUsers,name='verifiedusers'),
    path('dashboard/unverifiedusersbankdetails/<int:pk>', views.UnVerifiedUsersBankDetails,name='unverifiedusersbankdetails'),
    path('dashboard/unverifiedusers', views.UnVerifiedUsers,name='unverifiedusers'),
    path('dashboard/userdetails/<int:pk>', views.UserDetails,name='userdetails'),
    path('dashboard/donarslist', views.LatestDonars,name='donarslist'),

    path('dashboard/pendingwithdraw', views.PendingWithdraw,name='pendingwithdraw'),
    path('dashboard/confirmwithdraw/<int:pk>', views.ConfirmWithdraw,name='confirmwithdraw'),
    path('dashboard/readytowithdraw', views.ReadytoWithdraw,name='readytowithdraw'),
    path('dashboard/confirmreadytowithdraw/<int:pk>', views.ConfirmReadytoWithdraw,name='confirmreadytowithdraw'),
    path('dashboard/allwithdrawdone', views.AllWithdrawDone,name='allwithdrawdone'),

]
