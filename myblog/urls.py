
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myposts.urls')),
    path('userauth/', include('django.contrib.auth.urls')),
    path('userauth/', include('userauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
