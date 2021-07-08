from django.urls import path
from .views import *


app_name = "jobapplication"

urlpatterns = [
    path('', ProductListView.as_view(), name = 'home'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name = 'detail'),
    path('tocart/<int:pro_id>', AddToCartView.as_view(), name = 'detail'),

]
