from django.urls import path
from .views import *


app_name = "portalapp"

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('feedback/', Feedback.as_view(), name = 'feedback'),
    path('categories/', CategoryView.as_view(), name = 'categories'),
    path('cat-jobs/<str:cat>/', SpecificCategory.as_view(), name = 'catjobs'),
    path('single-job/<int:pk>/', SingleJob.as_view(), name = 'singlejob'),
    path('wishlist/', Wishlist.as_view(), name = 'wishlist'),
    path('savejob-<int:pk>/', SaveJob.as_view(), name = 'savejob'),

    # path('myview/', myview, name = 'myview'),
    
]
