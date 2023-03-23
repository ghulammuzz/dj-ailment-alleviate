from django.contrib import admin
from .models import Medicine

# Register your models here.

class MedicineAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'status', 'image')
    list_editable = ('name', 'status', 'image')

admin.site.register(Medicine, MedicineAdmin)