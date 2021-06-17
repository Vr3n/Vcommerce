from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Form for new user creation,
    """

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    """
    Form for user update.
    """

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
