from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm  
from .forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView

from portalapp.views import IndexView
from django.contrib.auth.forms import UserCreationForm

class ProfileView(IndexView):
    template_name = 'clients/profile.html'



class UserRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


    def post(self, request, *args, **kwargs):
            form_class = self.get_form_class()
            form = self.get_form(form_class)

            if form.is_valid():
                messages.info(
                    request, "Registered successfully"
                )
                return self.form_valid(form)
            
            else:
                return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Register"
        return context
        

class UserEditProfile(generic.UpdateView):
    form_class = UserEditProfileForm
    template_name = 'clients/Edit_profile.html'

    def get_success_url(self):
        return reverse_lazy('portalapp:profile', kwargs={'pk': self.object.pk})
    
    def get_object(self): 
        return self.request.user


@method_decorator(login_required, name = 'dispatch')
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('portalapp:index')
    # def get_success_url(self):
    #     return reverse_lazy('portalapp:profile', kwargs={'pk': self.object.pk})
    

    # def get_object(self): 
    #     return self.request.user
