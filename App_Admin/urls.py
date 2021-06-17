from django.urls import path
from App_Admin import views

app_name = 'App_Admin'

urlpatterns = [
    # path('organization/<slug:slug>/', views.OrgDashboard, name="OrganizationDashboard"),
    # path('organization/<slug:slug>/bankinformation', views.BankInformation, name="OrganizationBankInformation"),
    # path('organization/<slug:slug>/updatebankinformation', views.UpdateBankInformation, name="OrganizationUpdateBankInformation")
    # path('', views.Home, name='home'),
    # path('product/<pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('master',views.master,name='master'),
    path('adminhome',views.AdminHome,name='adminhome'),
    path('organizations',views.organizations,name='organizations'),
    path('verifiedusers',views.verifiedusers,name='verifiedusers'),
    path('generalusers',views.generalusers,name='generalusers'),
    path('eventsbyusers',views.eventsbyusers,name='eventsbyusers'),
    path('generalusers',views.eventsbyorganizations,name='eventsbyorganizations'),
]
