from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')

admin.site.register(User, UserAdmin)

class PeracikAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone_number', 'status', 'user')
admin.site.register(Peracik, PeracikAdmin)