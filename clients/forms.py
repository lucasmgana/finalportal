from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from django.db.models import fields
from portalapp.models import *


class UserRegisterForm(UserCreationForm):
    email           = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1       = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email',)


    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'




class UserEditProfileForm(UserChangeForm):
    username        = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email           = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'required':'required'}))
    first_name      = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name       = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login      = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # is_superuser    = forms.CharField(max_length=255, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_staff        = forms.CharField(max_length=255, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_active       = forms.CharField(max_length=255, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined     = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login')


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username           = forms.EmailField(widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'type':'text',
                            'placeholder': 'Enter username',
                            }), label='Username')
    password           = forms.EmailField(widget=forms.PasswordInput(attrs={
                            'class': 'form-control',
                            'type':'Password',
                            'placeholder': 'Enter password',
                            }))
    class Meta:
        model = User
        fields = '__all__'


