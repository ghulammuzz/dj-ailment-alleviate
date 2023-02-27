from django.contrib import admin
from .models import *

# Register your models here.
admin.AdminSite(name='PanelAdmin')
admin.site.register(Reader)
admin.site.register(Admin)
admin.site.register(Peracik)
admin.site.register(User)