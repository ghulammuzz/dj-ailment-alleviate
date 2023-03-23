from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from accounts.views import *
from category.views import *
from ingredient.views import *
from medicine.views import *

urlpatterns = [
    
    # admin and test
    path('admin/', admin.site.urls),
    
    # auth
    path("api/login/", PeracikLoginView.as_view()),
    path("api/register/", PeracikSignUpView.as_view()),
    
    # list category, ingredients, medicine
    path("category/", ListCategory.as_view()),
    
    path("ingredient", ListIngredient.as_view()),
    path("ingredient/<int:pk>", ListIngredient.as_view()),
    
    path("medicine/<int:pk>", ListMedicine.as_view()),
    path("medicine", ListMedicine.as_view()),
    
    # dashboard peracik
    path("dashboard/peracik", DashboardPeracik.as_view()),
    
    # media root
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),

]
