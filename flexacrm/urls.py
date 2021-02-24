from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from leads.views import landing_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace="leads")),
    path('', landing_page, name='landing-page'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)