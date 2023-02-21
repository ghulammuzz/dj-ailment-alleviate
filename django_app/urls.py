from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard', DashboardView.as_view({'get': 'list'})),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
