from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns=[
    path("register/",views.register, name="register"),
    path("login/",views.user_login, name="login"),
    path('logout/',views.user_logout, name="logout"),
    path('profile', views.profile, name="profile"),

    #password reset
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"), name="password_reset"),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_sent.html"), name= "password_reset_done"),
    path('password_reset/<str:uidb64>/<str:token>', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_form.html"), name="password_reset_confirm"),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete"),

    path("email_verification/<str:uidb64>/<str:token>", views.email_verification, name="email_verification"),
    path("email_verification_sent", views.email_verification_sent, name="email_verification_sent"),
    path("email_verification_success", views.email_verification_success, name="email_verification_success"),
    path("email_verification_failed", views.email_verification_failed, name="email_verification_failed"),
]