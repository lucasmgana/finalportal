from django.urls import path
from .views import *
app_name = "portalapp"

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('feedback/', Feedback.as_view(), name = 'feedback'),
    path('categories/', CategoryView.as_view(), name = 'categories'),
    path('catetory/<str:cat>/', SpecificCategory.as_view(), name = 'catjobs'),
    path('job/<int:pk>/', SingleJob.as_view(), name = 'singlejob'),
    
    path('profile-<int:pk>/', ProfileView.as_view(), name = 'profile'),
    path('applying-<int:pk>/', ApplicationView.as_view(), name = 'applying'),

    path('my-dashboard/', MyApplicationsView.as_view(), name = 'my-dashboard'),
    path('my-dashboard/<str:status>/', FilterView.as_view(), name = 'my-dashboard'),
    path('save-job/<int:pk>/', SaveJobView, name='savejob'),

    path('my-saves/', MySaveView.as_view(), name = 'my-saves'),
]
