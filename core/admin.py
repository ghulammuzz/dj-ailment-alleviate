from django.contrib import admin
from .models import *

label = 'Bahan'
admin.site.site_header = 'Admin Panel Ailmnent Alleviate'

class BahanAdmin(admin.ModelAdmin):
    list_display = ['nama_bahan','status', 'gambar']
    list_editable = ['gambar', 'status']
    list_filter = ['nama_bahan']
    search_fields = ['nama_bahan']
    list_per_page = 25

admin.site.register(Bahan, BahanAdmin)

class ObatAdmin(admin.ModelAdmin):
    list_display = ['nama_obat', 'status', 'peracik','cara_pembuatan', 'aturan_pemakaian', 'bahan_1', 'bahan_2', 'bahan_3', 'bahan_4', 'bahan_5', 'bahan_6', 'bahan_7','gambar']
    list_editable = ['cara_pembuatan', 'status', 'peracik','aturan_pemakaian','bahan_1', 'bahan_2', 'bahan_3', 'bahan_4', 'bahan_5', 'bahan_6', 'bahan_7', 'gambar']
    list_filter = ['nama_obat']
    search_fields = ['nama_obat']
    list_per_page = 25
    
admin.site.register(Obat, ObatAdmin)

# class GejalaAdmin(admin.ModelAdmin):
#     list_display = ['nama_gejala', 'gambar']
#     list_editable = ['gambar']
#     list_filter = ['nama_gejala']
#     search_fields = ['nama_gejala']
#     list_per_page = 25
    
# admin.site.register(Gejala, GejalaAdmin)