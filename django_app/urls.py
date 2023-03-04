from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from django.urls import path, include
from core.views import *

urlpatterns = [
    path('nganu/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('dashboard/', DashboardView.as_view()),
    path('api/peracik/dashboard', DashboardPeracikView.as_view()),
    path('api/peracik/create/', BuatObatView.as_view()),
    path('dashboard/<int:pk>', DashboardView.as_view()),
    path('bahan/<int:pk>/', BahanView.as_view()),
    path('bahan/', BahanView.as_view()),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]   
