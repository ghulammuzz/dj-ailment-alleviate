from django.contrib import admin
from .models import *

class BahanAdmin(admin.ModelAdmin):
    list_display = ['nama_bahan', 'gambar']
    list_editable = ['gambar']
    list_filter = ['nama_bahan']
    search_fields = ['nama_bahan']
    list_per_page = 25

admin.site.register(Bahan, BahanAdmin)

class ObatAdmin(admin.ModelAdmin):
    list_display = ['nama_obat', 'bahan_1', 'bahan_2', 'bahan_3', 'bahan_4', 'bahan_5', 'gambar']
    list_editable = ['bahan_1', 'bahan_2', 'bahan_3', 'bahan_4', 'bahan_5', 'gambar']
    list_filter = ['nama_obat']
    search_fields = ['nama_obat']
    list_per_page = 25
    
admin.site.register(Obat, ObatAdmin)