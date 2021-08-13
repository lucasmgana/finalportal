from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from django.db.models import fields
from portalapp.models import *
from .models import Seeker


gender = [
    ('male', 'male'),
    ('female', 'female'),
]

class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # middle_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # gender = forms.CharField(widget=forms.Select(choices = gender, attrs={'class': 'form-control'}))
    # profile_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    # phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # country = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)


    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        # self.fields['date_of_birth'].widget.attrs['type'] = 'date'
        # self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'



class UserEditProfileForm(UserChangeForm):
    username        = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email           = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'required':'required'}))
    first_name      = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name       = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

class UserSettings(forms.ModelForm):
    age        = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    date_of_birth      = forms.DateTimeField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    phone       = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Seeker
        fields = ('age', 'gender', 'date_of_birth', 'phone',)

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs['class'] = 'form-control'


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


