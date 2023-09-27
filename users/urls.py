from django.urls import path
from django.contrib.auth import views as auth_views

from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, verify, check_email, error, PasswordRecoveryStartView, password_recovery_check_email

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verify/<int:id_user>', verify),
    path('check_email', check_email, name='check_email'),
    path('error', error, name='error'),


    #path('login/password_recovery', password_recovery, name='password_recovery'),

    path('password_recovery/start', PasswordRecoveryStartView.as_view(), name='password_recovery_start'),
    path('password_recovery_check_email', password_recovery_check_email, name='password_recovery_check_email'),

    # path('password_recovery/<int:id_user>', password_recovery),

    #
    # path('reset_password/', UserForgotPasswordView.as_view(), name='password_reset_form'),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),


]