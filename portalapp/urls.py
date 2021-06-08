from django.urls import path
from .views import *


app_name = "portalapp"

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('about/', AboutUsView.as_view(), name = 'about-us'),
    path('adddcategory/', AddCategory.as_view(), name = 'adddcategory'),
    path('categories/', CategoryView.as_view(), name = 'categories'),
    path('cat-jobs/<str:cat>/', CatJobs.as_view(), name = 'catjobs'),
    path('single-job/<int:pk>/', SingleJob.as_view(), name = 'singlejob'),
    path('wishlist/', Wishlist.as_view(), name = 'wishlist'),
    path('userprofile/', ProfileView.as_view(), name = 'userprofile'),
    path('savejob-<int:pk>/', SaveJob.as_view(), name = 'savejob'),

    

    

    
]
