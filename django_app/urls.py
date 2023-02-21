from django.contrib import admin
from django.urls import path
from bahan.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', DashboardView.as_view()),
]
