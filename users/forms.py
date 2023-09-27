from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django import forms

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserResetPasswordForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar', 'cantry')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()


class UserForgotPasswordForm(PasswordResetForm):
    """
    Запрос на восстановление пароля
    """