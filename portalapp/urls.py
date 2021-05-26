from django.urls import path
from .views import *


app_name = "portalapp"

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('about/', AboutUsView.as_view(), name = 'about-us'),
    path('contact-us/', ContactUsView.as_view(), name = 'contact-us'),
    path('categories/', CategoryView.as_view(), name = 'categories'),
    
]
