from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('portalapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=True)),
    path('clients/', include('clients.urls'))
]


urlpatterns += static(settings.STATIC_URL, document_root = settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)