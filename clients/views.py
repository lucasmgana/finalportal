from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm  
from .forms import *
from django.contrib.auth.views import PasswordChangeView


class ProfileView(generic.TemplateView):
    template_name = 'clients/profile.html'



class UserRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('portalapp:index')


    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)

class UserEditProfile(generic.UpdateView):
    template_name = 'clients/Edit_profile_page.html'
    form_class = UserEditProfileForm
    success_url = reverse_lazy('portalapp:profile')

    
    def get_object(self):
        return self.request.user



class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('index')

