from django.urls import path
from App_Admin import views

app_name = 'App_Admin'

urlpatterns = [
    # path('organization/<slug:slug>/', views.OrgDashboard, name="OrganizationDashboard"),
    # path('organization/<slug:slug>/bankinformation', views.BankInformation, name="OrganizationBankInformation"),
    # path('organization/<slug:slug>/updatebankinformation', views.UpdateBankInformation, name="OrganizationUpdateBankInformation")
    # path('', views.Home, name='home'),
    # path('product/<pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('adminhome',views.AdminHome,name='adminhome'),
    path('adminhome1',views.AdminHome1,name='adminhome1')
]
