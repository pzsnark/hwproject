# from django import forms
# from django.contrib.auth.forms import AuthenticationForm, UsernameField
#
#
# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(
#         label='Пароль',
#         widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form-control'})
#     )

from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
from ads.models import Message
from django import forms


class LoginForm(AuthenticationForm):
    username = UsernameField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'autofocus': True,
        'placeholder': 'Имя пользователя',
        'class': 'form-control'
    }))

    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form-control'})
    )

    error_messages = {
        'invalid_login': 'Введен неправильный логин или пароль'
    }


class SignupForm(UserCreationForm):
    error_messages = {'password_mismatch': 'Пароли не совпадают'}

    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'})
    )

    password2 = forms.CharField(
        label='Подтверждение пароля',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}),
        help_text="Введите тот же пароль, что и выше",
    )

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}),
            'email': forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Email'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Error addresses must be unique.')
        return email


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст сообщения'})
        }
