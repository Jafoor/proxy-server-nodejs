
from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('register/', views.register , name='register'),
    path('register_organization/', views.register_organization , name='register_organization'),
    #path('profilehiddennow/', views.profile , name='profile'),
    path('login/', views.login_view , name='login'),
    path('logout/', views.logout_view , name='logout'),
    path('email/confirmation/<str:activation_key>/', views.email_confirm, name = 'email_activation'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name = 'App_Account/password_reset_form.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'App_Account/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'App_Account/password_reset_confirm.html'),name='password_reset_confirm'),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name = 'App_Account/password_reset_complete.html'),name='password_reset_complete'),

    path('user/profile/<slug:slug>', views.generaluserdashboard, name="profile"),
    path('user/profile/<slug:slug>/updateinfo', views.updatepersonalinfo, name="updateinfo"),
    ]
