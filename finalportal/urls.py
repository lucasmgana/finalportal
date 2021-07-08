from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('portalapp.urls')),
    path('clients/', include('django.contrib.auth.urls')),
    path('application/', include('jobapplication.urls')),
    path('clients/', include('clients.urls'))
    
]


urlpatterns += static(settings.STATIC_URL, document_root = settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)