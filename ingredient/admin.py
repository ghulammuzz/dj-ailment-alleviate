from django.contrib import admin
from .models import Ingredient

# Register your models here.

# Labeling the admin page
admin.site.site_header = "Peracik Admin"
admin.site.site_title = "Peracik Admin Portal"
admin.site.index_title = "Welcome to Peracik Admin Portal"

# Theme in admin page
# admin.site.enable_nav_sidebar = False

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'category')
    list_editable = ('status', 'category')

admin.site.register(Ingredient, IngredientAdmin)
