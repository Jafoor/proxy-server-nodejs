from django.urls import path
from App_Organization import views

app_name = 'App_Organization'

urlpatterns = [
    path('organization/<slug:slug>/', views.OrgDashboard, name="OrganizationDashboard"),
    path('organization/<slug:slug>/bankinformation', views.BankInformation, name="OrganizationBankInformation"),
    path('organization/<slug:slug>/updatebankinformation', views.UpdateBankInformation, name="OrganizationUpdateBankInformation"),
    path('organization/<slug:slug>/organizationinformation', views.Organizationformation, name="OrganizationInformation"),
    path('organization/<slug:slug>/updateorganizationinformation', views.UpdateOrganizationInformation, name="UpdateOrganizationInformation"),
    path('organization/<slug:slug>/organizationdocuments', views.OrganizationDocuments, name="OrganizationDocuments"),
    path('organization/<slug:slug>/updateorganizationdocuments', views.UpdateOrganizationDocuments, name="UpdateOrganizationDocuments"),

    path('organization/<slug:slug>/withdraw', views.WithdrawAmount, name="withdrawamount"),
    path('organization/<slug:slug>/withdrawlist', views.WithdrawList, name="withdrawlist"),

    # path('', views.Home, name='home'),
    # path('product/<pk>/', views.ProductDetail.as_view(), name='product_detail'),
]
